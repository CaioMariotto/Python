km=float(input('Informe a quantidade de KM '))
d=int(input('Informe a quantidade de dias alugados '))
kmr=km*0.15
dr=d*60
valor=kmr+dr

print('O valor total a ser pago é de R${:.2f}'.format(valor))
