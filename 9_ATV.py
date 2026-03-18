import os
os.system("cls")

# Variáveis para a média geral
soma_geral = 0
qtd_geral = 0

# Variáveis para os pares
soma_pares = 0
qtd_pares = 0

# Variáveis para os ímpares
qtd_impares = 0

print("Digite números inteiros (0 para encerrar):")

while True:
    numero = int(input("Número: "))

    if numero == 0:
        break  # O número zero encerra a leitura
    
    if numero < 0:
        print("Digite apenas números positivos!")
        continue

    # Atualiza os dados gerais
    soma_geral += numero
    qtd_geral += 1

    # Verifica se o número é par ou ímpar
    if numero % 2 == 0:
        soma_pares += numero
        qtd_pares += 1
    else:
        qtd_impares += 1

# Exibição dos resultados
print("-" * 30)

if qtd_geral > 0:
    print(f"a) Quantidade de Pares: {qtd_pares}")
    print(f"   Quantidade de Ímpares: {qtd_impares}")
    
    # Média dos pares (só calcula se houver algum par)
    if qtd_pares > 0:
        media_pares = soma_pares / qtd_pares
        print(f"b) Média dos valores pares: {media_pares:.2f}")
    else:
        print("b) Média dos pares: Nenhum número par foi digitado.")
    
    # Média geral
    media_geral = soma_geral / qtd_geral
    print(f"c) Média geral dos números: {media_geral:.2f}")
else:
    print("Nenhum número foi inserido.")