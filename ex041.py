'''leia o ano de nascimento de um atleta
e mostre a categoria de acordo com a idade'''

idade=int(input('Informe a sua idade: '))

if idade <= 9:
    print(f'Você esta na categoria MIRIM')
elif idade > 9 and idade < 14:
    print(f'Voce está na categoria INFANTIL')
elif idade >= 14 and idade < 19:
    print(f'Voce esta na categoria JUNIOR')
elif idade >= 19 and idade < 20:
    print(f'Voce esta na categoria SENIOR')
else:
    print(f'voce esta na categoria MASTER')