# solicitando ao usuário que insira 3 números:
num1 = int(input('Digite um número: '))
num2 = int(input('Digite mais um número: '))
num3 = int(input('Digite mais um número: '))

# fazendo as comparações para verificar qual é o maior:
if num1 > num2 and num1 > num3:
    print(f'O número {num1} é o maior!')
elif num2 > num3:
    print(f'O número {num2} é o maior!')
else:
    print(f'O número {num3} é o maior!')