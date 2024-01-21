# importanto a biblioteca random (aleatória)
import random

def verificacao(chute):
    if chute not in 'abcdefghijklmnopqrstuvwxyz' or len(chute) > 1:
        chute = input('Valor inserido inválido! Digite novamente: ')

def repetido(chute, tentativas):
    chute == True
    while chute:
        for char in tentativas:
            if chute == char:                    
                chute = input('Valor repetido! Digite novo valor: ')
        break
    chute = False   

def tentativa():
    tentativas = []
    chute = input('Digite uma letra: ')
    tentativas.append(chute)
    verificacao(chute)



    

# Criando uma lista com algumas espécies de animais
animais = ['elefante', 'camelo', 'zebra', 'rinoceronte', 'carneiro', 'tamandua', 'tartaruga', 'baleia', 'tucano', 'leopardo', 'macaco', 'coruja', 'hipopotamo', 'girafa', 'suricato', 'canguru', 'tatu', 'lontra', 'ornitorrinco']
random.shuffle(animais)   #usando a função random.shuffle da biblioteca importada para que a lista seja embaralhada
animal = animais[0].upper()     # escolhendo o primeiro item da lista

# Começando o jogo:
espacos = ''
print('Vamos jogar forca? Tente adivinhar a espécie do animal abaixo:\nVocê tem 6 tentativas!')
for letra in animal:
    espacos += '_ '
print(espacos)








