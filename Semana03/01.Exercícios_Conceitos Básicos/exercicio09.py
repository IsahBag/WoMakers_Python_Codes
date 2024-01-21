
# solicitando ao usuário que entre com o valor de horas de exercícios praticados em uma semana:
horassemana = int(input('Insira a quantidade média de horas de exercícios praticados em uma semana: '))

# convertando para minutos, considerando um mês de 30 dias:
minutosmes = ((horassemana / 7) * 30) * 60

# calculando a quantidade de calorias quiemadas e imprimindo o resultado:
print(f'Total de calorias queimadas no mês: {minutosmes*5:.2f}')