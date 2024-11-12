//Dia 1 - Desafio 7 Days of Code
//Arrays - Lista de Compras

const limiteAleatorio = 100;
const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let listaCompras = [];

//Adiciona um novo item a lista
const adicionarItem = (nomeItem, quantidade) => {
  const idItem = Math.floor(Math.random() * limiteAleatorio);

  listaCompras.push({ id: idItem, item: nomeItem, qtd: quantidade });
  console.log("Item cadastrado!");
};

//Remove um item da lista
const removerItem = (nomeItem) => {
  if (listaCompras.length === 0) {
    console.log("A lista de compras está vazia!");
  } else {
    const index = listaCompras.findIndex((item) => item.item === nomeItem);

    //findIndex() retorna -1 se o valor não for encontrado
    if (index !== -1) {
      listaCompras.splice(index, 1);
      console.log(`O item ${nomeItem} foi removido com sucesso!`);
    } else {
      console.log(`Item não encontrado!`);
    }
  }
};

//Lista os itens da lista
const listarItens = () => {
  if (listaCompras.length === 0) {
    console.log("A lista de compras está vazia!");
  } else {
    listaCompras.forEach((item) => {
      console.log(
        `ID: ${item.id}\nITEM: ${item.item}\nQUANTIDADE: ${item.qtd}`,
      );
    });
  }
};

//Menu
const menu = () => {
  rl.question(
    "Escolha uma opção:\n[1] Cadastrar Produto\n[2] Remover Produto\n[3] Listar Produtos\n[9] Sair\nR: ",
    (resp) => {
      const op = Number(resp);

      switch (op) {
        case 1:
          rl.question("Informe o nome do Item.\nR: ", (respItem) => {
            const nomeItem = respItem;

            rl.question(
              "Quantas unidades deste item serão cadastradas?\nR: ",
              (respQtd) => {
                const qtd = respQtd;
                adicionarItem(nomeItem, qtd);
                menu();
              },
            );
          });
          break;
        case 2:
          rl.question(
            "Informe o nome do Item a ser excluído.\nR:",
            (respExcluir) => {
              const itemExcluido = respExcluir;
              removerItem(itemExcluido);
              menu();
            },
          );
          break;
        case 3:
          console.log("\n---------- LISTA DE ITENS ----------\n");
          listarItens();
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

//Função Principal
const main = () => {
  menu();
};

module.exports = { main };
