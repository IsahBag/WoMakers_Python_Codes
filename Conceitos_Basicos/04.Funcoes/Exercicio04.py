"""EXERCÍCIO 4: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira, e calcule quanto poderia comprar de cada moeda estrangeira. Considere a tabela de conversão abaixo:
Dólar Americano: R$4,91
Peso Argentino: R$0,02
Dólar Australiano: R$3,18
Dólar Canadense: R$3,64
Franco Suiço: R$0,42
Euro: R$5,36
Libra esterlina: R$6,21"""

   
 iando as funções referentes a cada conversão separadamente:
def dolar_usa(v):
    return v / 4.91

def peso(v):
    return v / 0.02

def dolar_aus(v):
    return v / 3.18

def dolar_can(v):
    return v / 3.64

def franco(v):
    return v / 0.42

def euro(v):
    return v / 5.36

def libra(v):
    return v / 6.21

# Solicitando ao usuário que informe o valor que possui na carteira:
valor = float(input('Digite o valor que possui na carteira: R$ '))

# Chama as funções e imprime os resultados:
print(f'Com esse valor você pode comprar:\nDólar Americano: ${dolar_usa(valor):.2f}\nPeso Argentino: ${peso(valor):.2f}\nDólar Australiano: ${dolar_aus(valor):.2f}\nDólar Canadense: ${dolar_can(valor):.2f}\nFranco Suíço: ${franco(valor):.2f}\nEuro: ${euro(valor):.2f}\nLibra esterlina: ${libra(valor):.2f}')