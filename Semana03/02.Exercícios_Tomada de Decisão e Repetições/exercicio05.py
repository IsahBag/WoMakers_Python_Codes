# solicitando ao usuário que insira o valor de cada lado do triângulo
ladoa = float(input('Insira a medida do lado A do triângulo: '))
ladob = float(input('Insira a medida do lado B do triângulo: '))
ladoc = float(input('Insira a medida do lado C do triângulo: '))

# eliminando a hipótese de que os valores informados não formem um triângulo:
if ((ladoa + ladob) < ladoc) or ((ladoa + ladoc) < ladob) or ((ladob + ladoc) < ladoa):  
    print('Não forma um triângulo')

# Fazendo as comparações:
else:
    if ladoa == ladob == ladoc:
        print('Triângulo equilátero')
    elif ladoa == ladob or ladoa == ladoc or ladob == ladoc:
        print('Triângulo isósceles')
    else:
        print('Triângulo escaleno')