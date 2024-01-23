"""EXERCÍCIO 10: Faça um programa que utilize 4 variáveis como preferir e no final print uma mensagem amigável utilizando as variáveis criadas. Exemplos de variáveis: nome, idade, lugar, profissão.... Exemplo de retorno: Olá Maria, prazer te conhecer. Sou de São Paulo  também e estou migrando de área. Lembrando que para o retorno vamos usar print com as variáveis criadas e este texto é somente um exemplo, utilizem a criatividade"""


# Solicitando os dados ao usuário:
nome = (input('Digite seu nome: '))
cidade = (input('Digite a cidade em que você mora: '))
profissao = (input('Digite sua profissão: '))

# Imprimindo a mensagem personalizada:
print(f'Olá {nome} de {cidade}! É um prazer te ver por aqui!\nQue legal que você é {profissao}, assim podemos compartilhar nossas experiências.')