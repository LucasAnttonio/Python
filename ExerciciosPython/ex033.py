a = float(input('Primeiro valor: '))
b = float(input('Segundo valor: '))
c = float(input('Terceiro valor: '))

maior = a
menor = a

if b > a and b > c:
    maior = b

if c > a and c > b:
    maior = c

if b < a and b < c:
    menor = b

if c < a and c < b:
    menor = c

print(f'Maior valor: {maior}')
print(f'O menor valor: {menor}')
