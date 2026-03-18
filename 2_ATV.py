import os

os.system("cls")    


for i in range(3):
    print("Tentativa ", i + 1)
while True:
    login = input("Digite  o nome do usuário: ")
    senha = input("Digite a senha: ")
    if login == "admin" and senha == "1234":
        print("Login bem-sucedido!")
        break
    else:
        print("Login ou senha incorretos. Tente novamente.")
