"""EXERCÍCIO 2: Faça um programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N-Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso"""


# Solicitando ao usuário que informe o código referente ao turno
turno = input("Digite o turno em que você estuda (utilize M-matutino, V-Vespertino ou N-Noturno): ")

# Imprimindo a mensagem conforme o valor informado:
if turno == 'M':
    print("Bom dia!")
elif turno == 'V':
    print("Boa tarde!")
elif turno == 'N':
    print("Boa noite!")
else:
    print("Valor inválido!")