print('Bem vindo ao Controle de Estoque da Bicicletaria da Jhuly Bastos')
def cadastrarPeca(codigo): #dados para cadastrar peça
    nome = input("Digite o nome da peça: ")
    fabricante = input("Digite o fabricante da peça: ")
    valor = float(input("Digite o valor da peça: "))
#dados da peça
    peca = {
        "codigo": codigo,
        "nome": nome,
        "fabricante": fabricante,
        "valor": valor
    }

    return peca
#menu de opções
def consultarPeca(pecas):
    while True:
        print("\n--- Menu de Consulta ---")
        print("1. Consultar Todas as Peças")
        print("2. Consultar Peças por Código")
        print("3. Consultar Peças por Fabricante")
        print("4. Retornar")

        opcao = input("Digite a opção desejada: ")
#se o usuario digitar o opção 1 aparece sobre todas as peças
        if opcao == "1":
            if pecas:
                print("\n--- Todas as Peças ---")
                for peca in pecas:
                    print("Código:", peca["codigo"])
                    print("Nome:", peca["nome"])
                    print("Fabricante:", peca["fabricante"])
                    print("Valor: R$ %.2f" % peca["valor"])
                    print("--------------------")
            else:
                print("Não há peças cadastradas.") #caso não tenha nenhuma peça cadastrada
#opção de consultar as peças pelo código
        elif opcao == "2":
            codigo = input("Digite o código da peça: ")
            encontrada = False

            for peca in pecas:
                if peca["codigo"] == codigo:
                    print("\n--- Peça Encontrada ---")
                    print("Código:", peca["codigo"])
                    print("Nome:", peca["nome"])
                    print("Fabricante:", peca["fabricante"])
                    print("Valor: R$ %.2f" % peca["valor"]) # Valor em até duas casas decimais "%.2f"
                    encontrada = True
                    break

            if not encontrada:
                print("Nenhuma peça encontrada com o código", codigo) # Caso nenhuma peça seja encontrada
# Para procurar de acordo com o fabricante da peça
        elif opcao == "3":
            fabricante = input("Digite o fabricante da peça: ")
            encontrada = False

            print("\n--- Peças do Fabricante", fabricante, "---")
            for peca in pecas:
                if peca["fabricante"] == fabricante:
                    print("Código:", peca["codigo"])
                    print("Nome:", peca["nome"])
                    print("Fabricante:", peca["fabricante"])
                    print("Valor: R$ %.2f" % peca["valor"])
                    print("--------------------")
                    encontrada = True

            if not encontrada:
                print("Nenhuma peça encontrada do fabricante", fabricante) # caso nenhuma peça for encontrada

        elif opcao == "4": # ele retorna
            break

        else:
            print("Opção inválida. Digite uma opção válida.")

def removerPeca(pecas): # escolher peças para serem removidas
    codigo = input("Digite o código da peça a ser removida: ")
    removida = False

    for i, peca in enumerate(pecas):
        if peca["codigo"] == codigo:
            del pecas[i]
            print("Peça removida com sucesso.")
            removida = True
            break

    if not removida:
        print("Nenhuma peça encontrada com o código", codigo)

# Programa principal
pecas = []
codigo = 1

while True:
    print("\n--- Menu Principal ---")
    print("1. Cadastrar Peça")
    print("2. Consultar Peça")
    print("3. Remover Peça")
    print("4. Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        peca = cadastrarPeca(codigo)
        pecas.append(peca)
        codigo += 1
        print("Peça cadastrada com sucesso.")

    elif opcao == "2":
        consultarPeca(pecas)

    elif opcao == "3":
        removerPeca(pecas)

    elif opcao == "4":
        break

    else:
        print("Opção inválida. Digite uma opção válida.")