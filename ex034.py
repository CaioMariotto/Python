sal=int(input('Digite o seu salário: '))
if sal <= 1250:
    print('Seu salario sofreu reajuste de 10% agora é {:.2f}.'.format(sal+(sal*10/100)))
else:
    print('Seu salario sofreu reajuste de 15% e agora é {:.2f}.'.format(sal+(sal*15/100)))