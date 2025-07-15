#Elif

idade = int(input('Qual sua idade:'))

if idade < 18:
    print('Menor de idade')
elif idade>= 18 and idade <60:
    print('Maior de idade')
else:
    print('Idoso')


#Forma simplificada:

if idade < 18:
    print('Menor de idade')
elif 18<= idade <60:
    print('Maior de idade')
else:
    print('Idoso')



