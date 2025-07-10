mensagem = 'Este curso é muito bom'

#Metodos comuns em strings

print(mensagem.upper()) #upper é para tudo em letra maiuscula
print(mensagem.lower()) #lower é para tudo em letra miniscula
print(mensagem.strip()) #strip para remover os espaços
print(mensagem.replace('bom', 'Excelente')) #replace é para trocar alguma palavra por outra
print(mensagem.split()) # split separa palavra por palavra

mensagem2 = '''Geralmente eu trabalho
e estudo todos os dias, mas há dias 
que não é possível estudar quanto 
eu quero'''
print(mensagem2.replace('possível', 'impossível'))
print(mensagem2.upper())