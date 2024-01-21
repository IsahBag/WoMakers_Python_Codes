# Pedindo o nome do usuário:
nome = input('Digite seu nome: ')

# Convertendo a string para uma lista de caracteres e colocando-os em maiúsculas
lista = [letra.upper() for letra in list(nome)]

# Invertendo a lista
lista.reverse()

# Unindo os caracteres invertidos em uma string
inverso = ''.join(lista)

print(f'Nome invertido: {inverso}')