function filtrarTabela() {
    let input = document.getElementById("filtroInput");
    let filter = input.value.toUpperCase();
    let table = document.getElementById("tabelaMaquinas");
    let tr = table.getElementsByTagName("tr");

    // Percorre todas as linhas da tabela (exceto o cabeçalho)
    for (let i = 1; i < tr.length; i++) {
        let tdModelo = tr[i].getElementsByTagName("td")[0];
        let tdNumero = tr[i].getElementsByTagName("td")[1];
        
        if (tdModelo || tdNumero) {
            let textoModelo = tdModelo.textContent || tdModelo.innerText;
            let textoNumero = tdNumero.textContent || tdNumero.innerText;
            
            // Se o texto digitado estiver no Modelo OU no Número da Frota
            if (textoModelo.toUpperCase().indexOf(filter) > -1 || 
                textoNumero.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }
    }
}