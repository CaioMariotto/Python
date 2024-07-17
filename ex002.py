#Perguntar o nome e dar boas vindas e depois perguntar dia, mes e ano e montar a data de nascimento do usuario

from calendar import c


nome=input('Digite o seu nome ')
print ('Bem vindo ',nome)
dia=input ('Digite seu dia de nascimento ')
mes=input ('Digite o mes em que você nasceu ')
ano=input ('Qual o ano que você nasceu? ')
print (nome, 'nasceu no dia ',dia,'de',mes,'de',ano)
