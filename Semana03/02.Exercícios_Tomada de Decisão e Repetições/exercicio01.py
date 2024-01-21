# Solicitando ao usuário a inclusão de 2 números:
num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))

# Realizando as comparações para verificar qual o maior ou se são iguais
if num1 > num2:
    print(f"O número {num1} é o maior!")
elif num2 > num1:
    print(f"O número {num2} é o maior!")
else:
    print(f"Os números são iguais!")