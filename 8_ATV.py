import os
os.system("cls")

soma = 0
contador = 0

print("Cálculo de Média (Digite um número negativo para encerrar)")
print("-" * 50)

while True:
    numero = int(input("Digite um valor inteiro positivo: "))

    # Se o número for negativo, o programa para na hora
    if numero < 0:
        break
    
    # Caso contrário, ele soma e conta
    soma += numero
    contador += 1

# Só faz a média se pelo menos um número positivo foi digitado
if contador > 0:
    media = soma / contador
    print("-" * 50)
    print(f"Você digitou {contador} números.")
    print(f"A média aritmética é: {media:.2f}")
else:
    print("Nenhum número positivo foi inserido.")