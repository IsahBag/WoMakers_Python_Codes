# Solicitando ao usuário que entre com os valores:
valorhora = float(input('Informe o valor recebido por hora: R$'))
qtdhoras = int(input('Informe a quantidade de horas trabalhadas no mês: '))

# Realizando os calculos e imprimido o resultado:
print(f'O valor recebido no mês é de R$ {valorhora*qtdhoras:.2f}')