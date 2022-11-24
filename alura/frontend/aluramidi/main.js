// Função para tocar o áudio de cada som específico
function tocaSom(idAudio){
    document.querySelector(idAudio).play();
}

// Cria uma lista com todos os elementos html que incluem a tag .tecla
const listaDeTeclas = document.querySelectorAll('.tecla');

for (let contador = 0; contador < listaDeTeclas.length; contador++) {

    // Cria lista com od ids de cada audio
    const idAudios = `#som_${listaDeTeclas[contador].classList[1]}`;
    const teclas = listaDeTeclas[contador];
    //Reproduz o áudio
    teclas.onclick = function (){
        tocaSom(idAudios);
    }

    teclas.onekeydown = function (event){
        if (event.keyCode === 'Enter' || event.keyCode === 'Space'){
            teclas.classList.add('ativa');
        }
    }

    teclas.onkeyup = function (){
        teclas.classList.remove('ativa');
    }
}