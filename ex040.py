'''Crie um programa que leia duas notas de um aluno e calcule sua media
mostrando uma mensagem no final de acordo com a media atingida'''

n1 = float(input('Digite o valor da primeira nota:'))
n2 = float(input('Digite o valor da segunda nota:'))
media = (n1 + n2) // 2

if media <= 5.0:
    print(f'Você está reprovado.')
elif media >= 5 and media <= 7:
    print(f'Você está de recuperação.')
else:
    print(f'Você foi aprovado.')