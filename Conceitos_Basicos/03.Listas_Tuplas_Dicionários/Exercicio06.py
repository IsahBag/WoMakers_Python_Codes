"""EXERCÍCIO 6: Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas. Dica: lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas"""


# Pedindo o nome do usuário:
nome = input('Digite seu nome: ')

# Convertendo a string para uma lista de caracteres e colocando-os em maiúsculas
lista = [letra.upper() for letra in list(nome)]

# Invertendo a lista
lista.reverse()

# Unindo os caracteres invertidos em uma string
inverso = ''.join(lista)

print(f'Nome invertido: {inverso}')