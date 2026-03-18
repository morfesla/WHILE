import os

os.system("cls")

tentativas = 0
while True:
    login = input("Digite  o nome do usuário: ")
    senha = input("Digite a senha: ")
    if login == "admin" and senha == "1234":
        print("Login bem-sucedido!")
        break
    else:
        print("Login ou senha incorretos. Tente novamente.")
        tentativas += 1
        if tentativas >= 3:
            print("Número máximo de tentativas atingido. Programa encerrado.")
            break