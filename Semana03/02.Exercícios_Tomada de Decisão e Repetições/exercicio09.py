# solicitando ao usuário que informe um número:
num = int(input('Digite um número: '))

# atribuindo o valor zero às variáveis
pares = 0
impares = 0

# verficando a quantidade de pares e ímpares até que seja digitado 0:
while num != 0:
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    num = int(input('Digite mais um número: '))

# impressão dos resultados:
print(f'Quantidade de números pares: {pares}\nQuantidade de números ímpares: {impares}')