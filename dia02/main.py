class No:
    def __init__(self, paciente):
        self.paciente = paciente
        self.prox_paciente = None

class ListaEncadeada:

    def __init__(self):
        self.primeiro_paciente = None
        self.ultimo_paciente = None

    def adicionarPaciente(self, dados):
        novo_paciente = No(dados)

        if self.primeiro_paciente is None:
            self.primeiro_paciente = novo_paciente
            self.ultimo_paciente = novo_paciente
        else:
            self.ultimo_paciente.prox_paciente = novo_paciente
            self.ultimo_paciente = novo_paciente

    def listarPacientes(self):
        atual = self.primeiro_paciente
        i = 1

        while atual is not None:
            paciente = atual.paciente

            print(f"\nPaciente {i}:\n")
            print(f"ID Paciente: {paciente['id']}")
            print(f"Nome: {paciente['nome']}")
            print(f"Estado: {paciente['estado']}\n")

            i += 1
            atual = atual.prox_paciente

    def removerPacientes(self,nome):
        atual = self.primeiro_paciente
        anterior = None

        while atual is not None and atual.paciente['nome'] != nome:
            anterior = atual
            atual = atual.prox_paciente

        if atual is None:
            print("\nPaciente não encontrado.")
        else:
            if anterior is None:
                self.primeiro_paciente = atual.prox_paciente
            else:
                anterior.prox_paciente = atual.prox_paciente
        print("\nPaciente removido com sucesso.")


if __name__ == "__main__":
    paciente = ListaEncadeada()
    sair = 0

    try:
        while sair < 1:
            print("\n---------- SGH ----------\n")
            print("[1] Cadastrar paciente\n[2] Listar pacientes\n[3] Remover paciente\n\n[9]Sair\n")
            op = int(input("R: "))

            if op == 1:
                print("\n----- DADOS PACIENTE -----\n")

                print("ID (padrão ISA-123): ")
                id_paciente = input()

                print("Nome: ")
                nome = input()

                print("Estado de Saúde: ")
                estado_saude = input()

                dados = {'id': id_paciente, 'nome': nome, 'estado': estado_saude}
                paciente.adicionarPaciente(dados)

            elif op == 2:
                print("\n----- PACIENTES CADASTRADOS -----\n")
                paciente.listarPacientes()

            elif op == 3:
                nome = ""

                print("\nInforme o paciente que deseja remover: ")
                nome = str(input())

                paciente.removerPacientes(nome)


            elif op == 9:
                print("Fim do programa!")
                sair += 1

            else:
                print("Opção inválida!")

    except Exception as e:
        print(f"Falha na execução do programa: {e}")
