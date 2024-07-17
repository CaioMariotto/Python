km=int(input('Digite a quilometragem rodada: '))
lim=200

if km <= lim:
    print('Voce rodou {}km, seu pagamento será de {} reais.'.format(km,km*0.50))
else:
    print('Voce rodou {}km e seu pagamento será de {} reais.'.format(km,((km-lim)*0.45)+100))

