from listarItem import listarItem
from adicionarItem import adicionarItem
from removerItem import removerItem

lista_itens = []

def menu():

    sair = 0
    try:
        while(sair < 1):
            op = 0
    
            print("\n----------- MENU ----------\n")
            print("\n[1] Adicionar Item\n[2] Listar Itens\n[3] Remover Itens\n\n[9] Sair")

            op = int(input("\nR: "))

            # match é o equivalente ao switch em python
            match op:
                case 1:
                    print("\nProduto:\n")
                    nome = input()

                    print("\nQuantidade:\n")
                    quantidade = int(input())
         
                    adicionarItem(lista_itens, nome, quantidade)

                case 2:
                    if (len(lista_itens) == 0):
                        print("\nA lista está vazia.")
                    else:
                        listarItem(lista_itens)

                case 3:
                    if (len(lista_itens) == 0):
                        print("\nA lista está vazia.")
                    else:
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
