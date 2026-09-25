# regex solution for the exercise problem:
# Criar expressão regular para apanhar Strings Binárias que não contenham a subString "011"
#
# Explicação da expressão: ^(?!.*011)[01]*$
# ^   -> começa na primeira posição da string
# (?!.*011) -> "olha para a frente" e verifica se não existe "011" em qualquer parte da string
# [01]* -> permite qualquer sequência formada só por 0 e 1 (inclui string vazia)
# $ -> termina na última posição da string
#
# Ou seja: aceita só strings binárias sem a sequência "011".
# Exemplos:
#  "0"      -> aceita
#  "1010"   -> aceita
#  "011"    -> rejeita
#  "11011"  -> rejeita
#  "001010" -> aceita
^(?!.*011)[01]*$