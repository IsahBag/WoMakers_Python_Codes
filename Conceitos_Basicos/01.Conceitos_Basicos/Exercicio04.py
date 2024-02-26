"""EXERCÍCIO 4: Receba do usuário a quantidade de litros de combustível consumidos e a distância percorrida. Calcule e imprima o consumo médio em    km/l"""
 

# Solicitando ao usuário que informe a quantidade de litros consumida e a distância percorrida em uma viagem:
l = int(input('Informe a quantidade de litros consumida: '))
km = int(input('Informe a distância percorrida em quilometros: '))

# Realizando o cálculo e imprimindo o resultado:
print(f'O consumo médio foi de {km/l:.2f} km/l.')