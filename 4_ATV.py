import os
os.system("cls")

notas = [3]
contador = 1 # Começa na nota 1

while contador <= 3:
    nota = float(input(f"Digite a {contador}ª nota (0 a 10): "))
    
    # Verifica se a nota é válida
    if nota >= 0 and nota <= 10:
        notas.append(nota) # Adiciona a nota na lista
        contador += 1      # Soma +1 no contador para ir para a próxima nota
    else:
        print("Nota inválida! Tente novamente.")

# Calcula a média usando a lista
media = sum(notas) / 3

print("-" * 30)
print(f"Média Final: {media:.1f}")

# Verificação do resultado
if media >= 7:
    print("Situação: APROVADO")
elif media >= 5:
    print("Situação: RECUPERAÇÃO")
else:
    print("Situação: REPROVADO")