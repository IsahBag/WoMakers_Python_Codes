"""EXERCÍCIO 6: Vamos construir um jogo de forca. O programa escolherá aleatoriamente uma palavra secreta de umalista predefinida. A palavra secreta será representada por espaços em branco, um para cada letra da palavra.O jogador terá um número limitado de 6 tentativas. Em cada tentativa, o jogador pode fornecer uma letra. Se a letra estiver presente na palavra secreta, ela será revelada nas posições correspondentes. Se a letra não estiver na palavra, uma mensagem de erro deverá ser informada. Após um número máximo de erros, o jogador perde. O jogo continua até que o jogador adivinhe a palavra ou exceda o número máximo de tentativas. Dica: Você precisará importar uma biblioteca para resolver esse exercício"""


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








