"""EXERCÍCIO 7: Solicite ao usuário o peso em kg e a altura em metros. Calcule e imprima o Índice de Massa Corporal(IMC) usando a fórmula:     IMC=peso/(alturaxaltura)."""


# Solicitando ao usuário que entre com o valor de seu peso e altura:
peso = float(input('Insira seu penso em kg: '))
altura = float(input('Digite sua altura em metros: '))

# Calculando o IMC e imprimindo o resultado:
print(f'O valor do seu IMC é {peso/(altura**2):.1f}')