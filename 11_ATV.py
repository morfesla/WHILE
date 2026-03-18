import os
os.system("cls")
# Variáveis para armazenar os dados
total_familias = 0
soma_salarios = 0
soma_filhos = 0
maior_salario = 0
menor_salario = 0

while True:
    print("\n--- PESQUISA PREFEITURA ---")
    print("1 | Adicionar família")
    print("2 | Sair e exibir resultados")
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        os.system("cls")
        
        salario = float(input("Digite o salário da família: R$ "))
        filhos = int(input("Digite o número de filhos: "))

        # Acumulando dados
        total_familias += 1
        soma_salarios += salario
        soma_filhos += filhos

        # Lógica de Maior e Menor salário
        if total_familias == 1:
            maior_salario = salario
            menor_salario = salario
        else:
            if salario > maior_salario:
                maior_salario = salario
            if salario < menor_salario:
                menor_salario = salario
        
        print("\nDados registrados!")

    elif opcao == "2":
        os.system("cls")
        print("="*40)
        print("      RESULTADO FINAL DA PESQUISA")
        print("="*40)
        
        if total_familias > 0:
            media_salario = soma_salarios / total_familias
            media_filhos = soma_filhos / total_familias
            
            print(f"a) Total de famílias: {total_familias}")
            print(f"b) Média salarial: R$ {media_salario:.2f}")
            print(f"c) Média de filhos: {media_filhos:.1f}")
            print(f"d) Maior salário: R$ {maior_salario:.2f}")
            print(f"e) Menor salário: R$ {menor_salario:.2f}")
        else:
            print("Nenhuma família cadastrada.")
            
        print("="*40)
        break # Encerra o programa após exibir

    else:
        print("Opção inválida! Tente 1 ou 2.")