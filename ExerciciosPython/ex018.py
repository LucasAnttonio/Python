from math import sin, cos, tan, radians

angulo = radians(float(input('Digite o ângulo que você deseja: ')))
seno, cosseno, tangente = sin(angulo), cos(angulo), tan(angulo)

print(f'O ângulo de {angulo} tem o SENO de {seno:.2f}')
print(f'O ângulo de {angulo} tem o COSSENO de {cosseno:.2f}')
print(f'O ângulo de {angulo} tem a TANGENTE de {tangente:.2f}')
