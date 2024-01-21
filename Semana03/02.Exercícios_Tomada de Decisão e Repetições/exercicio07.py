# solicitando que o usuário entre com a idade:
idade = int(input('Informe sua idade: '))

# verificando se a idade é válida:
while idade < 0 or idade > 120:
    idade = int(input('Idade inválida! Insira novamente: '))

# verificando a idade e imprimindo a mensagem conforme valor informado:
if idade < 12:
    print('O(a) usuário(a) é uma criança!')
elif idade >= 12 and idade < 18:
    print('O(a) usuário(a) é um(a) adolescente!')
elif idade >= 18 and idade <= 65:
    print('O(a) usuário(a) é um(a) adulto(a)!')
else:
    print('O(a) usuário(a) é um(a) idoso(a)!')