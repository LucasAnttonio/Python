salario = float(input('Qual é o sálario do funcionario? R$'))

if salario <= 1250.00:
    desconto = salario + (salario * 15 / 100)
else:
    desconto = salario + (salario * 10 / 100)

print(f'Quem ganhava R${salario} passa a ganhar R${desconto} agora.')
