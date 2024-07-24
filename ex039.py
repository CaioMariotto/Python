from datetime import date

'''faça um programa que leia o ano de nascimento do usuario e 
de acordo com a idade informe:
- se ele ainda vai ter que se alistar ao exercito
- se é a hora de se alistar
- se ja passou do tempo do alistamento'''

ano_nasciento=int(input('Digite seu ano de nascimento: '))
def calcular_idade(ano_nascimento):
    ano_atual=date.today().year
    return ano_atual - ano_nasciento

idade=calcular_idade(ano_nasciento)

def verificar_alistamento(idade):

    if idade < 18:
        print('Voce ainda vai se alistar ao exercito.')
        
    elif idade == 18:
        print('Está na hora de se alistar.')
    else:
        print('Já passou do tempo de alistamento')


situação=verificar_alistamento(idade)
