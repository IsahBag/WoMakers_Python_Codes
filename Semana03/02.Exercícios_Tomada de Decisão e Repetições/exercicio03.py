# Solicitando ao usuário que informe o valor de uma nota:
nota = float(input('Digite uma nota entre 0 e 10: '))

# Laço para garantir que o valor digitado esteja dentro dos parâmetros informados:
while nota < 0.0 or nota > 10.0:
    nota = float(input('Digite uma nota entre 0 e 10: '))

print('Fim de programa')