# Definindo a função que irá fazer o reverso do número:
def reverso (n):
    lista = [num for num in list(n)]   # insere o número numa lista e o converte para uma lista de caracteres
    lista.reverse()     # invertendo o valor da lista
    rev = ''.join(lista)  # unindo os caracteres invertidos em uma string
    return rev

# Solicitando a entrada de valores pelo usuário:
num = input('Digite um número: ')

# imprimindo o resultado formatado chamando a função:
print(f'O inverso do número {num} é {reverso(num)}')