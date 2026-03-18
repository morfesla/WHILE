import os
os.system("cls")

total_conta = 0

while True:
    # Exibe o Menu
    print("----- CARDÁPIO -----")
    print("1 - Picanha       R$ 25,00")
    print("2 - Lasanha       R$ 20,00")
    print("3 - Strogonoff    R$ 18,00")
    print("4 - Bife Acebolado R$ 15,00")
    print("5 - Pão com ovo   R$ 5,00")
    print("-" * 20)

    # Escolha do prato
    escolha = input("Escolha o código do prato: ")

    # Verifica qual prato foi escolhido e soma ao total
    if escolha == "1":
        total_conta += 25
    elif escolha == "2":
        total_conta += 20
    elif escolha == "3":
        total_conta += 18
    elif escolha == "4":
        total_conta += 15
    elif escolha == "5":
        total_conta += 5
    else:
        print("Código inválido! Tente novamente.")
        continue # Faz o loop voltar para o início sem perguntar se quer continuar

    # Pergunta se quer continuar
    continuar = input("Deseja escolher outro prato? (s/n): ").lower()
    
    if continuar == "n":
        break # Quebra o loop e finaliza o programa

print("-" * 20)
print(f"Total a pagar: R$ {total_conta:.2f}")
print("Obrigado pela preferência!")