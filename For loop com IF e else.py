#For loop com IF e else

compra_confirmada= True
dados_compra= "Compra no valor de R$15.50 e entrega confirmada!"

for enviar in range (3):
    if compra_confirmada:
        print(dados_compra)
        print('Detalhes enviados para o seu email!')
        break #para não ficar repetindo a toa todas as mensagens
else:
    print('Falha na compra!')