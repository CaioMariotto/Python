#Pedir pro usuario informar uma metragem e printar essa metragem convertida em centimentros e metros.

m=float(input('Digite a metragem: '))
c=float(m*100)
mm=float(m*1000)

print('O valor digitado convertido para centimetros é de: {} e em milimetros é de {}'.format(c,mm))