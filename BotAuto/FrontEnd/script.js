
function proximaEtapa(etapaAtual) {
 
    document.getElementById(`etapa${etapaAtual}`).style.display = 'none';
    
    
    document.getElementById(`etapa${etapaAtual + 1}`).style.display = 'block';
    
 
    window.scrollTo(0, 0);
}


function voltarEtapa(etapaAtual) {
 
    document.getElementById(`etapa${etapaAtual}`).style.display = 'none';
    
   
    document.getElementById(`etapa${etapaAtual - 1}`).style.display = 'block';
    
   
    window.scrollTo(0, 0);
}


function cancelar() {
  
    document.getElementById('etapa2').style.display = 'none';
    document.getElementById('etapa3').style.display = 'none';
    

    document.getElementById('etapa1').style.display = 'block';
    
   
    const inputs = document.querySelectorAll('input, textarea');
    inputs.forEach(input => {
        input.value = '';
    });
    

    window.scrollTo(0, 0);
}


function concluirCadastro() {

    document.getElementById('successModal').style.display = 'flex';
    

    console.log('Produto cadastrado com sucesso!');
}


function fecharModal() {

    document.getElementById('successModal').style.display = 'none';
    

    cancelar();
}