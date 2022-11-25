const somar = document.querySelector("#somar");
const subtrair = document.querySelector("#subtrair");
const braco = document.querySelector("#braco");
const blindagem = document.querySelector("#blindagem");

somar.addEventListener("click", function() {
    braco.value = parseInt(braco.value) + 1;
})
