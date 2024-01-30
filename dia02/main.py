dados = [{"id": "", "nome": "", "estado": ""}]

# Criando a estrutura principal de uma lista encadeada
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
            atual = self.primeiro_paciente
            while atual.prox_paciente is not None:
                atual= atual.prox_paciente
            atual.prox_paciente = novo_paciente
            self.ultimo_paciente = novo_paciente
                
    def removerPaciente():
        pass

    def listarPacientes(self):
        atual = self.primeiro_paciente

        while atual is not None:

            pacientes = atual.paciente

            for i in range(len(dados)):
                print(f"\nPaciente {i}: \n")
                for paciente in pacientes:
                    print(f"ID Paciente: {paciente['id']}") 
                    print(f"Nome: {paciente['nome']}")
                    print(f"Estado: {paciente['estado']}")
            i=+1
            atual = atual.prox_paciente 

if __name__ == "__main__":

    paciente = ListaEncadeada()
    sair = 0

    try:
        while sair < 1:
            print("\n---------- SGH ----------\n")
            print("[1] Cadastrar paciente\n[2] Listar pacientes\n[3] Remover paciente\n\n[9]Sair\n")
            op = int(input("R: "))

            match op:
                case 1:
                    print("\n----- DADOS PACIENTE -----\n")

                    print("ID (padrão ISA-123): ")
                    id_paciente = input()

                    print("Nome: ")
                    nome = input()

                    print("Estado de Saúde: ")
                    estado_saude = input()

                    dados = [{'id': id_paciente, 
                              'nome': nome, 
                              'estado': estado_saude}]

                    paciente.adicionarPaciente(dados)            
                case 2:
                    print("\n----- PACIENTES CADASTRADOS -----\n")
                    paciente.listarPacientes()
                case 3:
                    pass
                case 9:
                    print("Fim do programa!")
                    sair += 1
                case _:
                    pass
    except Exception as e:
        print(f"Falha na execução do programa: {e}")
