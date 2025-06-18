function ordenarTabela(coluna) {
  const tabela = document.getElementById("tabelaProdutos");
  let ordenando = true;
  let ordem = "asc";

  while (ordenando) {
    ordenando = false;
    const linhas = tabela.rows;

    for (let i = 1; i < linhas.length - 1; i++) {
      let troca = false;
      let x = linhas[i].getElementsByTagName("TD")[coluna];
      let y = linhas[i + 1].getElementsByTagName("TD")[coluna];

      if (
        ordem === "asc" &&
        x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()
      ) {
        troca = true;
        break;
      } else if (
        ordem === "desc" &&
        x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()
      ) {
        troca = true;
        break;
      }
    }

    if (troca) {
      linhas[i].parentNode.insertBefore(linhas[i + 1], linhas[i]);
      ordenando = true;
    } else {
      if (ordem === "asc") {
        ordem = "desc";
        ordenando = true;
      }
    }
  }
}
