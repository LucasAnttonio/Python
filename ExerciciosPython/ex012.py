preco = float(input('Qual é o preço do produto? R$'))
desconto = 15
preco_descontado = preco - (preco * desconto / 100)
print(f'O produto que custava R${preco:.2f}, na promoção com desconto de {desconto}% vai custar R${preco_descontado:.2f}')
