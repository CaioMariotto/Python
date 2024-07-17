frase=str(input('Digite a frase: ')).strip()

print('Seu nome em maiúsculu é:',frase.upper())
print('Seu nome em minúsculo é:',frase.lower())
print('Seu nome tem ao todo {} letras.'.format(len(frase)-frase.count(' ')))
dividido=frase.split()
print('Seu primeiro nome é {} e ele tem {} letras.'.format(dividido[0],len(dividido[0])))
#print('Seu primeiro nome tem {} letras.'.format(frase.find(' ')))