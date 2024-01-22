def listarItem(lista_itens):

    print("\n----------- LISTA DE ITENS ----------\n")
    print("PRODUTO\t\t\tQUANTIDADE")
    for i in lista_itens:
        print(f"{i['nome']}\t\t\t{i['quantidade']}")
