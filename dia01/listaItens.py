lista_itens = []

def adicionarItem(lista_itens, nome, quantidade):
    
    lista_itens.append({"nome": nome, "quantidade": quantidade})

def listarItem(lista_itens):

    print("\n----------- LISTA DE ITENS ----------\n")
    for i in lista_itens:
        print(f"Nome: {i['nome']}\nQuantidade: {i['quantidade']}")

def removerItem(lista_itens, produto):

    if (lista_itens == None):
        print("\nSua lista está vazia.")
    else:
        if(produto != lista_itens["nome"]):
            print("Produto não encontrado.")
        else:
            lista_itens.pop(produto)
