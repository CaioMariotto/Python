'''calcule o valor a ser paga em um produto, consiferando o preço normal
e a condição de pagamento'''

compra=float(input('Digite o total da sua compra: '))
pag=int(input('Informe a condição de pagamente:\n 1. a vista ou cheque - 10%\n 2. a vista no cartão - 5%\n 3. até 2x no cartão - preço normal\n 4. 3x ou mais no cartao - 20% de juros.\n'))

if pag == 1:
    print('O total foi de R${:.2f}, com o desconto sua compra fica R${:.2f}'.format(compra,compra-(compra*0.10)))
elif pag ==2:
    print('O total foi de R${:.2f}, com o desconto sua compra fica R${:.2f}'.format(compra,compra-(compra*0.05)))
elif pag == 3:
    print('O total da sua compra foi de R${}, nao tem desconto.')
else:
    print('O total foi de R${}, com 20% de juros sua compra fica R${}.'.format(compra,compra+(compra*0.20)))