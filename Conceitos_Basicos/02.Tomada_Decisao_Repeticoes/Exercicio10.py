"""EXERCÍCIO 10: Faça um programa que lê três números inteiros e os mostra em ordem crescente."""

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

menor = min(num1, num2, num3)
maior = max(num1, num2, num3)
meio = (num1 + num2 + num3) - menor - maior

print(f'Os números em ordem crescente são: {menor}, {meio}, {maior}')