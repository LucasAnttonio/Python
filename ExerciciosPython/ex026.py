frase = input('Digite uma frase: ').strip().lower()
frase = frase.replace('á', 'a')

vezes = frase.count('a')
posicao_letra = frase.find('a') + 1
ultima_letra = frase.rfind('a', 0, len(frase)) + 1

print(f'A letra A aprace {vezes} vezes na frase.')
print(f'A primeira letra A apareceu na posição {posicao_letra}')
print(f'A última letra A apareceu na posição {ultima_letra}')
