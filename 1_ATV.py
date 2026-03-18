import os

os.system("cls")
#soma das notas
soma = 0
#quantidade de notas
quantidade_notas = 2
#loop para entrada das notas
for i in range(quantidade_notas):
    while True:
        #entrada da nota
        nota = float(input("Digite a nota do aluno: "))
        #verifica se a nota é valida
        if nota >= 0 and nota <= 10:
            soma += nota
            break
        #se a nota for invalida
        else:
            print("Nota invalida.")
            print("tente novamente... \n")
#calculo da media
media = soma / quantidade_notas

print("Nota do aluno: ", media)
# Fim do programa