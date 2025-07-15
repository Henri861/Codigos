#Pratica de If e Else

#Exemplo 1

#Controle de temperatura

C = int(input('Qual é a temperatura hoje?'))

if C < 10:
    print('Está congelando!!!')
elif 10<= C <20:
    print('Está um pouco frio, realmente!')
else:
    print('Rapaz, tá ficando quente, compre um ar condicionado!')