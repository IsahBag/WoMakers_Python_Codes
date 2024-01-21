#solicitando ao usuário que entre com o login
login = input('Digite o nome do usuário: ')
while login != 'admin':  
    login = input('Usuário não encontrado! Tente novamente: ') 

# solicitação para entrar com a senha
senha = input('Digite a senha: ')   
while senha != 'admin123': # #garantindo que o usuário digite o valor correto
    senha = input('Senha incorreta! Tente novamente: ')

# impressão do resultado:
print('Acesso autorizado!')