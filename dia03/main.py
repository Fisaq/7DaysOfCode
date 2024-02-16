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

    def adicionarProdutos(self,dados_produto):
        novo_produto = No(dados_produto)

        if self.primeiro_produto is None:
            self.primeiro_produto = novo_produto
            self.ultimo_produto = novo_produto
        else:
            self.ultimo_produto.prox_produto = novo_produto
            self.ultimo_produto = novo_produto

    def removerProduto(self,nome_produto):
        atual = self.primeiro_produto

        while atual is not None and atual.produto['nome'] != nome_produto:
            atual = atual.prox_produto

        if atual is None:
            print("\nProduto não encontrado.")

        else:

            if atual.prod_anterior is None:
                self.primeiro_produto = atual.prox_produto
            else:
                atual.prod_anterior.prox_produto = atual.prox_produto

            if atual.prox_produto is not None:
                atual.prox_produto.prod_anterior = atual.prod_anterior

            print("\nProduto removido com sucesso.")    
            
        

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
                    print("Informe o produto que deseja cadastrar no estoque: ")
                    
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
