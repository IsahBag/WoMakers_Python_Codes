# Solicitando ao usuário para entrar com o valor do salário bruto:
bruto = float(input('Digite o valor do salário bruto: R$ '))

# Criando variáveis com os valores de desconto correspondentem a cada faixa de salário:
vfaixa2 = (2826.65 - 1903.98) * 0.075
vfaixa3 = (3751.05 - 2826.65) * 0.15
vfaixa4 = (4664.68 - 3751.06) * 0.225

print(vfaixa2)
print(vfaixa3)
print(vfaixa4)

# Realizando os cálculos de acordo com a alíquota de cada faixa de valor:
if (bruto <= 1903.98):
    liq = bruto
elif (1903.99 <= bruto and bruto <= 2826.65):
    liq = bruto - ((bruto - 1903.98) * 0.075)
elif (2826.66 <= bruto and bruto <= 3751.05):
    liq = bruto - ((bruto - 2826.66) * 0.15) - vfaixa2
elif (3751.06 <= bruto and bruto <= 4664.68):
    liq = bruto - ((bruto - 3751.06) * 0.225) - vfaixa2 - vfaixa3
else:
    liq = bruto - ((bruto - 4664.68) * 0.275) - vfaixa3 - vfaixa4

# Imprimindo o resultado:
print(f'O valor do salário líquido será R$ {liq:.2f}')