"""EXERCÍCIO 5: Escreva um programa que calcule o salário líquido. Lembrando de declarar o salário bruto e o percentual de desconto do Imposto de Renda.
●Renda até R$1.903,98: isento de imposto de renda;
●Renda entre R$1.903,99 e R$2.826,65: alíquota de 7,5%;
●Renda entre R$2.826,66 e R$3.751,05: alíquota de 15%;
●Renda entre R$3.751,06 e R$4.664,68: alíquota de 22,5%;
●Renda acima de R$4.664,68: alíquota máxima de27,5%."""


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