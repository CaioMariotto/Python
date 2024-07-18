num=int(input('Digite um número: '))
num2=int(input('Digite outro número: '))
num3=int(input('Digite um último número: '))

maior=max(num, num2, num3)
menor=min(num, num2, num3)

print('O menor número é {}.'.format(menor))
print('O maior número é {}.'.format(maior))