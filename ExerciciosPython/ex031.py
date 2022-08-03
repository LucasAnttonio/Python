dis = float(input('Qual a distancia da viagem? '))

print(f'Você está prestes a começar uma viagem de {dis}Km/h')

if dis > 200:
    print(f'E o preço da sua passagem será de R${dis * 0.45:.2f}')
else:
    print(f'E o preço da sua passagem será de R${dis * 0.50:.2f}')
