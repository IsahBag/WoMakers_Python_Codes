# Criando a lista:
listademedias = []

# Adicionando as médias de 5 alunos na lista criada
for i in range(0, 5, 1):    
    notas = input('Digite as notas do aluno (separadas por espaço): ')
    notas = notas.split()  # Separando as notas
    soma = 0
    for nota in notas:
        soma += float(nota)
    media = soma / len(notas) # Divindo a soma de todas as notas pela quantidade de elementos na lista
    listademedias.append(media)

# Fazendo a contagem de alunos que tiraram mais do que 7,0
alunos = 0
for media in listademedias:
    if media >= 7.0:
        alunos += 1

# Imprimindo os resultados:    
print(f'Médias: {listademedias}')
print(f'Número de aluno com média maior ou igual a 7.0: {alunos}')