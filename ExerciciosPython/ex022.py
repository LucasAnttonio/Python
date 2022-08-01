name = input('Digite seu nome completo: ').strip().split()
upper_name = ' '.join(name).upper()
lower_name = ' '.join(name).lower()
length_name = len(''.join(name))
first_name = name[0]
last_name = name[-1] # or name.pop()


print('Analizando seu nome...')
print(f'Seu nome em maiúsculas é {upper_name}')
print(f'Seu nome em minúsculas é {lower_name}')
print(f'Seu nome tem ao todo {length_name} letras')
print(f'Seu primeiro nome é {first_name} e ele tem {len(first_name)}')
print(f'Seu ultimo nome é {last_name}')
