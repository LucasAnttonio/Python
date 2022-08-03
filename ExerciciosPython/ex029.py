speed_car = float(input('Qual é a velocidade atual do carro? -> '))

if speed_car > 80.0:
    print(f'MULTADO! Você excedeu o limite permitido que é de {speed_car}Km/h')
    print(f'Você deve pagar uma multa de R${(speed_car - 80) * 7:.2f}')

print('Tenha um bom dia! Dirija com segurança!')
