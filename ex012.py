preco=float(input('Digite o preço total da compra: '))
desconto=float(preco*0.05)
precototal=preco-desconto
print('O total da compra com desconto é R${:.2f}'.format(precototal))
