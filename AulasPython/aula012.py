nome = input('Qual é o seu nome? ')

if nome == 'Lucas':
    print('Que nome bonito :)')
elif nome == 'Gustavo' or nome == 'José' or nome == 'Maria':
    print('Seu nome é bem popular no Brazil.')
elif nome == 'Whindersson':
    print('Que nome feio :(')
elif nome in 'Ana Júlia Luana Paula':
    print('Belo nome feminino XD')
else:
    print('Seu nome é bem normal :/')

print(f'Tenha um bom dia, {nome}!')
