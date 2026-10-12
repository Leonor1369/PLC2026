# Exemplo de teste
# 2025-02-20 by jcr 
from Teoricas.classe_afd import AutomatoFinitoDeterminista

# Define estados, alfabeto, ftransicao, estado inicial, e conjunto de estados finais
estados = {'A', 'B', 'C'}
alfabeto = {'0', '1'}
ftransicao = {'A': {'0': 'B', '1': 'C'}, 'B': {'0': 'A', '1': 'C'}, 'C': {'0': 'C', '1': 'C'}}
estado_inicial = 'A'
estados_finais = {'C'}

# Cria a instância do AFD
fsa = AutomatoFinitoDeterminista(estados, alfabeto, ftransicao, estado_inicial, estados_finais)

# Processa as sequências de input
input_sequence1 = '00101'
result1 = fsa.process_input(input_sequence1)
print(f"Resultado para '{input_sequence1}': {result1}")

input_sequence2 = '110'
result2 = fsa.process_input(input_sequence2)
print(f"Resultado para '{input_sequence2}': {result2}")
