# Inicializar com um Nó que referencia o próximo Nó e o Anterior
class No:
    def __init__(self, produto):
        self.produto = produto
        self.prox_produto = None
        self.prod_anterior = None

class ListaDuplamenteLigada:

    # Inicializa a class com o primeiro e o ultimo item da lista vazios
    def __init__(self):
        self.primeiro_produto = None
        self.ultimo_produto = None

    def adicionarProdutos():
        pass

    def removerProduto():
        pass

    def listarProduto():
        pass

    def atualizarQuantidade():
        pass

if __name__ == "__main__":

    produto = ListaDuplamenteLigada()
    sair = 0

    try:
        while sair < 1:
            print("\n---- GERENCIAMENTO DE ESTOQUE ----\n")
            print("[1] Adicionar produto\n[2] Listar produtos\n[3] Remover produtos [4] Atualizar quantidade\n\n[9] Sair\n")
            op = int(input("R: "))

            match op:
                case 1:
                    pass
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    pass
                case 9:
                    print("Fim do programa!")
                    sair += 1
                case _:
                    print("\nOpção inválida.")

    except Exception as e:
        print(f"Falha na execução do programa: {e}")
