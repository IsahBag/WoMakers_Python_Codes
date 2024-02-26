"""EXERCÍCIO 6: Vamos construir um jogo de forca. O programa escolherá aleatoriamente uma palavra secreta de umalista predefinida. A palavra secreta será representada por espaços em branco, um para cada letra da palavra.O jogador terá um número limitado de 6 tentativas. Em cada tentativa, o jogador pode fornecer uma letra. Se a letra estiver presente na palavra secreta, ela será revelada nas posições correspondentes. Se a letra não estiver na palavra, uma mensagem de erro deverá ser informada. Após um número máximo de erros, o jogador perde. O jogo continua até que o jogador adivinhe a palavra ou exceda o número máximo de tentativas. Dica: Você precisará importar uma biblioteca para resolver esse exercício"""


# Importanto a biblioteca random (aleatória)
import random

def verificacao(chute):
    while len(chute) != 1 or not chute.isalpha():
        chute = input('Valor inserido inválido! Digite novamente: ').upper()
    return chute

def tentativa_repetida(chute, tentativas):
    while chute in tentativas:
        chute = input('Valor repetido! Digite novo valor: ').upper()
    return chute

animais = ['elefante', 'camelo', 'zebra', 'rinoceronte', 'carneiro', 'tamandua', 'tartaruga', 'baleia', 'tucano', 'leopardo', 'macaco', 'coruja', 'hipopotamo', 'girafa', 'suricato', 'canguru', 'tatu', 'lontra', 'ornitorrinco']
random.shuffle(animais)
animal = list(animais[0].upper())

espacos = ['_'] * len(animal)
tentativas = []
vidas = 6

print('Vamos jogar forca? Tente adivinhar a espécie do animal abaixo:\nVocê tem 6 tentativas!')

while '_' in espacos and vidas > 0:
    print(' '.join(espacos))
    chute = input('Digite uma letra: ').upper()
    chute = verificacao(chute)
    chute = tentativa_repetida(chute, tentativas)
    tentativas.append(chute)
    
    if chute not in animal:
        vidas -= 1
        print('Letra não encontrada. Você tem', vidas, 'tentativas restantes.')
    else:
        for i in range(len(animal)):
            if chute == animal[i]:
                espacos[i] = chute
    
if '_' not in espacos:
    print(f'Parabéns! Você acertou o animal: {" ".join(animal)}!')
else:
    print(f'Você perdeu! A palavra era {" ".join(animal)}!')