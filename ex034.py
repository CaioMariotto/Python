sal=int(input('Digite o seu salário: '))


if sal>1250:
    print('Seu salario sofreu reajuste de 10% agora é {}.'.format((sal+(sal*0.10))))
else:
    print('Seu salario sofreu reajuste de 15% e agora é{}.',format((sal+(sal*0.15))))