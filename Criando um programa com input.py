#Captura do valor do produto

valor_produto = float(input('Qual é o valor do produto:'))

#Calcula o valor com 10% de acrescimo
valor_com_acrescimo = valor_produto * 1.10
#Exibir o valor final da tela
print(f' O valor final do produto com acrescimo é: R$ {valor_com_acrescimo:.2f}.')#Adicione (:2f) 2 ou qualquer número, de acordo com a quantidade de casas decimais 
#que deseja na resposta
