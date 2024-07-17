#Pedir para o usuário digitar algo e depois trazer informações sobre o que foi digitado.
#type, alpha, lower, space, num e title.

n=input('Digite algo: ')
print('O tipo desse valor é ', type(n))
print('É alfabetico? ', n.isalpha())
print('É minúsculo? ',n.islower())
print('Tem espaço? ',n.isspace())
print('É número? ', n.isalnum())
print('Esta capitalizada? ', n.istitle())