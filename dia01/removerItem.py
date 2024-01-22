def removerItem(lista_itens, produto):

    encontrado = None

    for prod in lista_itens:
        if (prod["nome"] == produto):
            encontrado = prod
            break

    if (encontrado != None):
        lista_itens.remove(encontrado)
        print(f"Item {encontrado['nome']} removido.")
    else:
        print("Produto não encontrado.")
