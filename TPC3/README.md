# TPC3 — Analisador léxico

**Autora:** Leonor Silva de Sousa — A109820

O programa `ana_lex.py` gera um tokenizer a partir das definições em
`token_def.json`. O tokenizer reconhece números, variáveis, identificadores,
strings, palavras reservadas e delimitadores. Ignora espaços e comentários.

Para gerar e executar o tokenizer, a partir da raiz do repositório:

```bash
python3 TPC3/ana_lex.py TPC3/token_def.json > TPC3/tokenizer_gerado.py
python3 TPC3/tokenizer_gerado.py < TPC3/text.py
```
