#Pedir para o usuário digitar a largura e altura, realizar o calculo de M² e passar a quantidade de tinta necessaria para aquela metragem.

l=float(input('Digite a largura da parede: '))
a=float(input('Digite a altura da parede: '))
aa=l*a
t=aa/2

print('A área da sua parede é de {}m², você precisará de {} litros de tinta'.format(aa,t))