import os

os.system("cls")

def obter_nota(ordem):
    while True:
        try:
            nota = float(input(f"Digite a {ordem}ª nota (0 a 10): "))
            if 0 <= nota <= 10:
                return nota
            else:
                print("Nota inválida! Por favor, digite um valor entre 0 e 10.")
        except ValueError:
            print("Entrada inválida! Digite apenas números.")

# Coleta das notas
nota1 = obter_nota(1)
nota2 = obter_nota(2)
nota3 = obter_nota(3)

# Cálculo da média
media = (nota1 + nota2 + nota3) / 3

print("-" * 30)
print(f"Média Final: {media:.2f}")

# Verificação da situação
if media >= 7:
    print("Situação: APROVADO")
elif 5 <= media < 7:
    print("Situação: RECUPERAÇÃO")
else:
    print("Situação: REPROVADO")