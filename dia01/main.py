from modulo_lista import lista_itens, adicionarItem,listarItem, removerItem

def menu():

    sair = 0
    try:
        while(sair < 1):
            op = 0
    
            print("\n----------- LISTA DE ITENS ----------\n")
            print("\n[1] Adicionar Item\n[2] Listar Itens\n[3] Remover Itens\n\n[9] Sair")

            op = int(input("\nR: "))

            # match é o equivalente ao switch em python
            match op:
                case 1:
                    print("\nProduto:")
                    nome = input()

                    print("\nQuantidade: ")
                    quantidade = int(input())
         
                    adicionarItem(lista_itens, nome, quantidade)

                case 2:
                    listarItem(lista_itens)

                case 3:
                    print("\nInforme o nome do produto que deseja remover: ")
                    prod = input("\nR: ")

                    removerItem(lista_itens, prod)

                case 9:
                    print("Fim do programa!")
                    sair+=1
                    
                case _:
                    print("\nOpção inválida!")              
    except:
        print("")

if __name__ == "__main__":

    menu()
