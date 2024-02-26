"""EXERCÍCIO 1: Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos"""

   
# Definindo a função que realizará a soma:
def soma(a,b,c):
    return a + b + c

# Solicitando ao usuário que entre com os valores:
num1 = int(input('Digite um número: '))
num2 = int(input('Digite um outro número: '))
num3 = int(input('Digite mais um número: '))

# Chamando a função e atribundo o resultado do retorno a uma variável:
resultado = soma(num1,num2,num3)

# Imprimindo o resultado:
print(f'O resultado da soma é {resultado}')