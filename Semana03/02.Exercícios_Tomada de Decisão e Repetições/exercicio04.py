# Solicitando que o usuário insira uma nota
nota = float(input('Digite uma nota entre 0 e 10: '))

# verificando se o valor inserito está dentro dos parâmetros:
while nota < 0 or nota > 10:
    nota = float(input('Digite uma nota entre 0 e 10: '))

# verificando o valor e imprimindo o resultado:
if nota >= 7.0:
    print('Aprovado!')
else:
    print('Reprovado!')