import os
os.system("cls")

soma_notas = 0
contador = 0  # Este contador vai contar quantas notas foram inseridas

while True:
    nota = float(input("Digite a nota: "))
    soma_notas += nota  # Acumula a nota na soma total
    contador += 1       # Conta que mais uma nota foi inserida
    
    # Pergunta se o usuário quer continuar
    resposta = input("Deseja inserir mais uma nota? (S/N): ").upper()
    
    if resposta == "N":
        break  # Sai do laço se a resposta for "N"

# Cálculo da média aritmética
# Usamos o 'contador' para dividir, pois ele sabe quantas notas foram digitadas
if contador > 0:
    media = soma_notas / contador
    print("-" * 30)
    print(f"Quantidade de notas inseridas: {contador}")
    print(f"A média aritmética é: {media:.2f}")
else:
    print("Nenhuma nota foi inserida.")