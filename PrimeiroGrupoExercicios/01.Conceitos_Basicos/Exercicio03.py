"""EXERCÍCIO 3: Faça um programa que peça a quantidade de quilômetros, transforme em metros, centímetros e milímetros."""


# Solicitando ao usuário entrar com o valor em quilometros:
km = int(input('Digite um valor em quilometros: '))

# Resposta com as conversões:
print(f'O valor informado corresponde a {km*1000} metros, {km*100000} centímetros e {km*1000000} milímetros')