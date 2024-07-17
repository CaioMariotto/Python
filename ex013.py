#Pedir para o usuário informar o salario e aplicar um reajuste de 15%, depois informar o salario atualizado.

salario=float(input('Digite o seu salário: '))
desconto=float(salario*0.15)
salatualizado=float(salario+desconto)

print('Seu salário com o aumento é de R${}'.format(salatualizado))