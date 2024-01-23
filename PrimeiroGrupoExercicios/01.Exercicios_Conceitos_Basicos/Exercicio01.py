"""EXERCÍCIO 1: Faça um programa que peça dois números, realize as principais operações soma, subtração, multiplicação e divisão"""


# Solicitando para os usuários entrarem com os números:
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

# Imprimindo os resultados e executando os cálculos numa mesma linha de comando:
print(f'Os resultados obtidos foram:\n{num1}+{num2}={num1+num2}\n{num1}-{num2}={num1-num2}\n{num1}x{num2}={num1*num2}\n{num1}/{num2}={num1/num2:.2f}')