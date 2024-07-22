import datetime

'''faça um programa que leia o ano de nascimento do usuario e 
de acordo com a idade informe:
- se ele ainda vai ter que se alistar ao exercito
- se é a hora de se alistar
- se ja passou do tempo do alistamento'''

ano=int(input('Digite seu ano de nascimento: '))
mes=int(input('Digite seu mes de nascimento: '))
dia=int(input('Digite seu dia de nascimento: '))
data=datetime.datetime(ano,mes,dia)
atual=datetime.datetime.now()
dif1= data - atual
dif2= atual - data

if dif1:
    print('Voce ainda vai se alistar ao exercito.')
    print('Faltam {} dias para o prazo de alistamento se encerrar.'.format(dif1))
elif dif2:
    print('Está na hora de se alistar.')
else:
    print('Já passou do tempo de alistamento')
    print('Faz {} dias que voce deveria ter se alistado.'.format(dif2))
