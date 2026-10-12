import json
import re
import sys


GENERATED_TOKENIZER = '''import json
import re
import sys

TOKEN_DEFS = __TOKEN_DEFS__
TOKEN_REGEX = re.compile(
    "|".join(
        f"(?P<T{index}>{token['expreg']})"
        for index, token in enumerate(TOKEN_DEFS)
    )
)


def tokenize(input_string):
    tokens = []
    position = 0
    line = 1

    while position < len(input_string):
        match = TOKEN_REGEX.match(input_string, position)
        if match is None:
            raise ValueError(f"No token matches input at offset {position}")
        if match.end() == position:
            raise ValueError(f"Token matched empty input at offset {position}")

        token_index = next(
            index
            for index in range(len(TOKEN_DEFS))
            if match.group(f"T{index}") is not None
        )
        token = TOKEN_DEFS[token_index]
        value = match.group()
        start = position

        if token["id"] not in ("SKIP", "Comment"):
            tokens.append((token["id"], value, line, (start, match.end())))

        line += value.count("\\n")
        position = match.end()

    return tokens


if __name__ == "__main__":
    source = sys.stdin.read()
    for token in tokenize(source):
        print(token)
'''


def main():
    if len(sys.argv) != 2:
        print("Usage: python ana_lex.py <token_def.json>", file=sys.stderr)
        return 1

    filename = sys.argv[1]
    try:
        with open(filename, "r", encoding="utf-8") as token_file:
            tokens = json.load(token_file)
    except OSError as error:
        print(f"Error reading '{filename}': {error}", file=sys.stderr)
        return 1
    except json.JSONDecodeError as error:
        print(f"Error: '{filename}' is not valid JSON: {error}", file=sys.stderr)
        return 1

    if not isinstance(tokens, list) or not tokens:
        print("Error: token definitions must be a non-empty JSON array.", file=sys.stderr)
        return 1

    token_ids = set()
    for index, token in enumerate(tokens):
        if (
            not isinstance(token, dict)
            or not isinstance(token.get("id"), str)
            or not isinstance(token.get("expreg"), str)
        ):
            print(
                f"Error: token definition {index} needs string 'id' and 'expreg' fields.",
                file=sys.stderr,
            )
            return 1
        if token["id"] in token_ids:
            print(f"Error: duplicate token id '{token['id']}'.", file=sys.stderr)
            return 1
        token_ids.add(token["id"])

    try:
        for token in tokens:
            re.compile(token["expreg"])
    except re.error as error:
        print(f"Error: invalid token regular expression: {error}", file=sys.stderr)
        return 1

    definitions = json.dumps(tokens, ensure_ascii=False)
    print(GENERATED_TOKENIZER.replace("__TOKEN_DEFS__", definitions), end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
