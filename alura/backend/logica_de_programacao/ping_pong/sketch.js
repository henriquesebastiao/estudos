// Características Bolinha
let xBolinha = 300;
let yBolinha = 200;
let diametro = 16;
let raio = 8;
let velocidadeXBolinha = 5;
let velocidadeYBolinha = 6;

//Características Minha Raquete
let xMinhaRaquete = 5;
let yMinhaRaquete = 150;
let comprimentoMinhaRaquete = 6;
let alturaMinhaRaquete = 90;

// Características Raquete Oponente
let xRaqueteOponente = 600 - 11;
let yRaqueteOponente = 150;
let alturaRaqueteOponente = 90;
let comprimentoRaqueteOponente = 6;
let velocidadeYRaqueteOponente = 6;

function setup() {
  createCanvas(600, 400);
}

function draw() {
  // Define cor de background
  background(0);

  // Desenha e movimenta bolinha
  circle(xBolinha, yBolinha, diametro);
  movimentaBolinha();

  // Desenha e movimenta minha raquete
  rect(
    xMinhaRaquete,
    yMinhaRaquete,
    comprimentoMinhaRaquete,
    alturaMinhaRaquete
  );
  movimentaMinhaRaquete();

  // Verifica se bolinha colide com a minha raquete
  verificaColisoMinhaRaqueteBiblioteca();

  // Desenha e movimenta raquete do oponente
  rect(
    xRaqueteOponente,
    yRaqueteOponente,
    comprimentoRaqueteOponente,
    alturaRaqueteOponente
  );
  movimentaRaqueteOponente();
  
  // Verifica se bolinha colide com raquete oponente
  verificaColisaoRaqueteOponenteBiblioteca();
}

function movimentaBolinha() {
  xBolinha += velocidadeXBolinha;
  yBolinha += velocidadeYBolinha;

  if (xBolinha > 600 - 8 || xBolinha < 8) {
    velocidadeXBolinha *= -1;
  }

  if (yBolinha > 400 - 8 || yBolinha < 8) {
    velocidadeYBolinha *= -1;
  }
}
function movimentaRaqueteOponente() {
  yRaqueteOponente += velocidadeYRaqueteOponente;

  if (yRaqueteOponente > 310 || yRaqueteOponente < 0) {
    velocidadeYRaqueteOponente *= -1;
  }
}
function movimentaMinhaRaquete() {
  if (keyIsDown(UP_ARROW)) {
    yMinhaRaquete -= 6;
  }
  if (keyIsDown(DOWN_ARROW)) {
    yMinhaRaquete += 6;
  }
}
function verificaColisaoRaquete() {
  // Verifica colisão com minha raquete
  // Verifica colisão raquete oponente
}

function verificaColisoMinhaRaqueteBiblioteca() {
  colidiu = collideRectCircle(
    xMinhaRaquete,
    yMinhaRaquete,
    comprimentoMinhaRaquete,
    alturaMinhaRaquete,
    xBolinha,
    yBolinha,
    raio
  );
  if (colidiu) {
    velocidadeXBolinha *= -1;
  }
}

function verificaColisaoRaqueteOponenteBiblioteca() {
    colidiu = collideRectCircle(
      xRaqueteOponente,
      yRaqueteOponente,
      comprimentoRaqueteOponente,
      alturaRaqueteOponente,
      xBolinha,
      yBolinha,
      raio
    );
  if (colidiu){
    velocidadeXBolinha *= -1;
  }
  }