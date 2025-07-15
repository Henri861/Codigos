#ogin

usuario_1 ='admin'
usuario_1_senha = '123456'

usuario = input("Digite o seu nome de usuario:")
senha = input("Digite a sua senha:")

if usuario == usuario_1 and senha == usuario_1_senha:
    print("Login OK")
else:
    print("Usuario ou senha incorretos.")

#Os sinais de iguais juntos são auto explicativos.
