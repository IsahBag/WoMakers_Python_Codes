# Solicitando ao usuário informar a distância até o destino:
dist = float(input('Informe a distância em quilometros até o destino: '))

# Calculando o tempo em minutos:
taviao = dist / 600 * 60
tcarro = dist / 100  * 60  
tonibus = dist / 80 * 60

# Convertendo os minutos em horas, mantendo o resto como minutos para formatar a saída:
print(f'Os tempos estimados de deslocamento são:\nAvião: {int(taviao//60)}:{int(taviao%60):02d} hora(s)\nCarro: {int(tcarro//60)}:{int(tcarro%60):02d} hora(s)\nÔnibus: {int(tonibus//60)}:{int(tonibus%60):02d} hora(s)')
