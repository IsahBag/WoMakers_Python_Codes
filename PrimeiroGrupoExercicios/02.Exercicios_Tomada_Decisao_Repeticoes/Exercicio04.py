"""EXERCÍCIO 4: Implemente um programa que classifique um aluno com base em sua pontuação em um exame. O programa deverá solicitar uma nota de 0 a 10. Se a pontuação for maior ou igual a 7, o aluno é aprovado; caso contrário, é reprovado"""


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