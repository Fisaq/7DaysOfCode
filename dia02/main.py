class No:

    def __init__(self, valor):
        self.valor = valor
        self.proximoNo = None # Próximo inicia-se vazio

class ListaLigada:

    def __init__(self, valor):
        self.primeiroNo = valor


    def adicionarNo(self,valor):
        novo_no = No(valor)

        if self.primeiroNo is None:
            self.primeiroNo = novo_no
        else:
            atual = self.primeiroNo
            while atual.proximoNo is not None:
                atual = self.proximoNo
            atual.proximoNo = novo_no

    def impimiNo(self):
        valor_atual = self.primeiroNo
        while valor_atual is not None:
            print(valor_atual.valor)
            valor_atual = valor_atual.primeiroNo

class Paciente:

    def __init__ (self, id_paciente, nome, estado_saude):
        self.id = id_paciente
        self.nome = nome
        self.estado_saude = estado_saude

    def adiconarPaciente():
        pass

    def removerPaciente():
        pass

    def listarPacientes():
        pass
