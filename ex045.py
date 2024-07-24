from random import choice

pedra = 'pedra'
papel = 'papel'
tesoura = 'tesoura'
lista = [pedra,papel,tesoura]
pc=choice(lista)

jogador=str(input('Escolha pedra, papel ou tesoura: '))
print('O cumputador escolheu {} '.format(pc))

if jogador == pedra and pc == papel:
    print('Voce perdeu')
elif jogador == pedra and pc == tesoura:
    print('Voce ganhou!')
elif jogador == papel and pc == tesoura:
    print('Voce perdeu!')
elif jogador == papel and pc == pedra:
    print('Voce perdeu!')
elif jogador == tesoura and pc == papel:
    print('Voce ganhou!')
elif jogador == tesoura and pc == pedra:
    print('Voce perdeu')
else:
    print('Empate!')