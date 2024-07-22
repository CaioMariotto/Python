
num=int(input('Digite um número qualquer: '))
conv=int(input('Digite a base de conversão que deseja:\n 1 - Binário\n 2 - Octagonal\n 3 - Hexadecimal\n '))


if conv == 1:
   print('O número convertido para binário é: {}'.format(bin(num)))
elif conv != 1 and conv != 3:
    print('O número convertido para octagonal é: {}.'.format(oct(num)))
else:
    print('O npumero convertido para hexadecimal é: {}.'.format(hex(num)))
    