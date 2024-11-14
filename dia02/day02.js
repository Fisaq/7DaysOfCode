//Dia 2 - Desafio 7 Days of Code
//Lista Simplesmente Encadeada - Gerenciamento de Pacientes

const maxId = 2000;
const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

//Estrutura do No
class Paciente {
  constructor(id, nome, estadoSaude) {
    this.id = id;
    this.nome = nome;
    this.estado = estadoSaude;
    this.proxPaciente = null;
  }
}
//Estrutura da Lista Simplesmete Encadeada
class ListaEncadeada {
  constructor() {
    this.head = null;
    this.tamanho = 0;
  }

  //Método para adicionar um novo paciente na lista
  adicionarPaciente(nome, estadoSaude) {
    const idPaciente = Math.floor(Math.random() * maxId);

    const novoPaciente = new Paciente(idPaciente, nome, estadoSaude);

    if (this.head === null) {
      this.head = novoPaciente;
    } else {
      let pacienteAtual = this.head;

      while (pacienteAtual.proxPaciente !== null) {
        pacienteAtual.proxPaciente = pacienteAtual.proxPaciente.proxPaciente;
      }
      pacienteAtual.proxPaciente = novoPaciente;
    }
  }

  //Método para adicionar um novo paciente na lista
  removerPaciente(nomePaciente) {
    if (this.head === null) {
      console.log("Não há pacientes cadastrados.");
    }

    if (this.head === nomePaciente) {
      this.head = this.head.proxPaciente;
      this.tamanho--;
      console.log(`O paciente ${nomePaciente} foi removido da lista.`);
    }

    let pacienteAtual = this.head;
    while (
      pacienteAtual.proxPaciente !== null &&
      pacienteAtual.proxPaciente.nome !== nome
    ) {
      pacienteAtual = pacienteAtual.proxPaciente;
    }

    if (pacienteAtual.proxPaciente !== null) {
      pacienteAtual.proxPaciente = pacienteAtual.proxPaciente.proxPaciente;
      this.tamanho--;
      console.log(`O paciente ${nomePaciente} foi removido da lista.`);
    } else {
      console.log(`Paciente ${nomePaciente} não encontrado.`);
    }
  }

  //Método para adicionar um novo paciente na lista
  listarPacientesEmOrdem() {
    if (this.head === null) {
      console.log("Não há pacientes cadastrados.");
    } else {
      let pacienteAtual = this.head;
      while (pacienteAtual.proxPaciente !== null) {
        console.log(
          `ID: ${pacienteAtual.id}\nNOME: ${pacienteAtual.nome}\nESTADO: ${pacienteAtual.estado}`,
        );
      }
    }
  }
}
const menu = () => {
  
  rl.question(
    "Escolha uma opção:\n[1] Adicionar Paciente na Fila\n[2] Remover Paciente\n[3] Listar Pacientes\n[9] Sair\nR: ",
    (resp) => {
      const op = Number(resp);

      switch (op) {
        case 1:
          rl.question("Informe o nome do Paciente.\nR: ", (respNomePac) => {
            const nomePaciente = respNomePac;

            rl.question(
              "Qual o estado de saúde do Paciente?\nR: ",
              (respEstado) => {
                const estado = respEstado;
                adicionarPaciente(nomePaciente, estado);
                menu();
              },
            );
          });
          break;
        case 2:
          rl.question(
            "Informe o nome do Paciente a ser removido.\nR:",
            (respPacRemove) => {
              const pacienteRemove = respPacRemove;
              removerPaciente(pacienteRemove);
              menu();
            },
          );
          break;
        case 3:
          console.log("\n---------- LISTA DE PACIENTES ----------\n");
          listarPacientesEmOrdem();
          menu();
          break;
        case 9:
          console.log("Fim do Programa!");
          rl.close();
          break;
        default:
          console.log("Opção inválida!");
          menu();
          break;
      }
    },
  );
};

const main = () => {
  menu();
};

module.exports = { main };
