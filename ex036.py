'''o programa vai perguntar o valor da casa.
o salario do comprador e informar a quatidade de anos para terminar de pagar.

calcule o valor da prestação mensal, sabendo que nao pode exceder 30% do salario,
se exceder o emprestimo é negado'''

valor=float(input('Informe o valor total da casa. '))
salario=float(input('Por favor, agora informe o seu salário '))
parcela=int(input('Agora informe a quantidade de anos que deseja pagar '))
pres=salario-(salario*0.70)

if valor <= (pres*(parcela*12)):
    print('emprestimo aprovado.')
else:
    print('Emprestimo negado.')