#Pedir para o usuário informar o KM rodado e a quanditade de dias alugados. 
#Depois realizar o calculo sendo que cada km rodado é R$0.15 e cada dia alugado é R$60.00

km=float(input('Informe a quantidade de KM '))
d=int(input('Informe a quantidade de dias alugados '))
kmr=km*0.15
dr=d*60
valor=kmr+dr

print('O valor total a ser pago é de R${:.2f}'.format(valor))
