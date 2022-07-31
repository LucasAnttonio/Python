salario = float(input('Qual é o salario do funcionário? R$'))
aumento = 20
salario_aumentado = salario + (salario * aumento / 100)
print(f'Um funcionário que ganhava R${salario:.2f}, com {aumento}% aumento, passa a receber R${salario_aumentado:.2f}')
