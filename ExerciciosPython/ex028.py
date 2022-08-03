from random import randint
from time import sleep

ran = randint(0, 5)

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)

num = int(input('Em que número eu pensei? -> '))
print('PROCESSANDO...')
sleep(1)

if ran == num:
    print(f'PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'GANHEI! Eu penssei no número {ran} e não no {num}!')
