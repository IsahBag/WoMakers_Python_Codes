"""EXERCÍCIO 1: Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são: 
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como"Inocente""""


# Criando a lista com as perguntas:
lista = ['Telefonou para a vítima? ', 'Esteve no local do crime? ', 'Mora perto da vítima? ', 'Devia para a vítima? ', 'Já trabalhou com a vítima? ']

# Fazendo a contagem:
sim = 0
nao = 0
for i in lista:    
    resp = input(i)
    if resp == 'nao':
        nao += 1
    else:
        sim += 1

# Mostrando o resultado conforme a quantidade de sim e não:
if sim == 2:
    print('Suspeito')
elif sim == 3 or sim == 4:
    print('Cúmplice')
elif sim == 5:
    print('Culpado')
else:
    print('Inocente')