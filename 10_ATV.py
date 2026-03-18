import os

os.system("cls")
# Variáveis para armazenar os dados
soma_salarios = 0
total_pessoas = 0
maior_idade = 0
menor_idade = 0
mulheres_salario_alto = 0

while True:
    print("\n--- MENU DE PESQUISA ---")
    print("1 | Adicionar pessoa")
    print("2 | Exibir resultados")
    print("3 | Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        os.system("cls") # Limpa o terminal ao adicionar
        
        idade = int(input("Digite a idade: "))
        sexo = input("Digite o sexo (M/F): ").upper()
        salario = float(input("Digite o salário: "))

        # a) Dados para a média de salário
        soma_salarios += salario
        total_pessoas += 1

        # b) Lógica de Maior e Menor idade
        if total_pessoas == 1: # Se for a primeira pessoa, a idade dela é a maior e a menor ao mesmo tempo
            maior_idade = idade
            menor_idade = idade
        else:
            if idade > maior_idade:
                maior_idade = idade
            if idade < menor_idade:
                menor_idade = idade

        # c) Mulheres com salário >= 5000
        if sexo == "F" and salario >= 5000:
            mulheres_salario_alto += 1
        
        print("\nDados registrados com sucesso!")

    elif opcao == "2":
        print("\n" + "="*30)
        print("      RESULTADOS")
        print("="*30)
        
        if total_pessoas > 0:
            media = soma_salarios / total_pessoas
            print(f"a) Média de salário: R$ {media:.2f}")
            print(f"b) Maior idade: {maior_idade} anos")
            print(f"   Menor idade: {menor_idade} anos")
            print(f"c) Mulheres com salário >= R$ 5.000: {mulheres_salario_alto}")
        else:
            print("Nenhum dado cadastrado ainda.")
        print("="*30)

    elif opcao == "3":
        print("Saindo do programa...")
        break
    
    else:
        print("Opção inválida!")