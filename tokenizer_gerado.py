import json
import re
import sys

TOKEN_DEFS = [{"id": "valor numerico", "expreg": "\\d+"}, {"id": "identificador de variavel", "expreg": "\\?[a-zA-Z0-9]+"}, {"id": "identificador de linguagem", "expreg": "@[A-Za-z0-9]{2}"}, {"id": "SKIP", "expreg": "\\s+"}, {"id": "STRING", "expreg": "('[^']*')|(\"[^\"]*\")"}, {"id": "Comment", "expreg": "\\#.*"}, {"id": "Reserved word", "expreg": "(select|where|LIMIT|OFFSET|ORDER|BY|ASC|DESC|AND|OR|NOT|BETWEEN|IN|IS|NULL|LIKE)(?![a-zA-Z0-9])"}, {"id": "identificador de conceito", "expreg": "[a-zA-Z0-9]+"}, {"id": "delimitador", "expreg": "\\.|\\{|\\}"}, {"id": "ERRO", "expreg": "."}]
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

        line += value.count("\n")
        position = match.end()

    return tokens


if __name__ == "__main__":
    source = sys.stdin.read()
    for token in tokenize(source):
        print(token)
