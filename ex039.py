from datetime import date

'''faça um programa que leia o ano de nascimento do usuario e 
de acordo com a idade informe:
- se ele ainda vai ter que se alistar ao exercito
- se é a hora de se alistar
- se ja passou do tempo do alistamento'''
ano_atual=date.today().year
ano_nasciento=int(input('Digite seu ano de nascimento: '))
idade=ano_atual-ano_nasciento

if idade == 18:
        print('Está na hora de se alistar.') 
elif idade < 18:
        saldo= 18 - idade
        ano = saldo+ano_atual 
        print('Voce ainda precisa se alistar ao exercito.')
        print('Seu alistamento será em {}'.format(ano))
else:
        saldo = idade - 18
        ano = ano_atual-saldo
        print('Já passou do tempo de alistamento.')
        print('Voce deveria ter se alistado em {}'.format(ano))
