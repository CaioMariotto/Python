frase=str(input('Digita uma frase: ')).strip().upper()

print('Nessa frase aparece a letra "A" {} vezes.'.format(frase.count('A')))
print('A letra "A" aparece na posição: {}'.format(frase.find('A')+1))
print('A ultima letra "A" apareceu {}'.format(frase.rfind('A')+1))