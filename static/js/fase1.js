const A = document.getElementById("A");
const B = document.getElementById("B");
const C = document.getElementById("C");
const D = document.getElementById("D");
const alternativas = document.querySelectorAll(".botao");
const pergunta = document.getElementById('pergunta')
pontuacaoHTML = document.getElementById("pontuacao");
sequenciaHTML = document.getElementById("sequencia");
var pontuacao = 100;
var sequenciaAcerto = 0;

var listaExercicios = JSON.parse(document.getElementById("listaExercicios").value);
var numeroExercicio = 1;
console.log(listaExercicios[0].enunciado)
console.log(listaExercicios)
carregarExercicio(1)

alternativas.forEach((botao) => {//percorre cada botão

    botao.addEventListener("click", function() {//adiciona o evento de clique

        const respostaCorreta = listaExercicios[numeroExercicio - 1].resposta.toLowerCase();//pega a resposta do exercício atual e coloca em minúscula
        
        if(botao.id.toLowerCase() === respostaCorreta) {//compara o id do botão clicado com a resposta 
            botao.classList.add("acerto");//adiciona a classe correto
            desabilitarAlternativas()
            sequenciaAcerto++
            pontuacao += 10 * sequenciaAcerto
            numeroExercicio++
            pontuacaoHTML.innerHTML = `Pontos: ${pontuacao}`;
            sequenciaHTML.innerHTML = `<i class="fa-solid fa-square-check fa-beat" style="color: #0e2349;"></i>sequência: ${sequenciaAcerto}`;
            
            
        } 
        else {
            botao.classList.add("erro");//adiciona a classe errado
            pontuacao -= 25
            sequenciaAcerto = 0
        }
    })
})

// continuar.addEventListener("click", function() {
//     numeroExercicio++;
//     carregarExercicio(numeroExercicio);
// })




// Funções de auxilio
function iniciar() {
    carregarExercicio(numeroExercicio);
}

function carregarExercicio(num) {
    pergunta.innerText = listaExercicios[num-1].enunciado;
    A.innerText = listaExercicios[num-1].alternativaA;
    B.innerText = listaExercicios[num-1].alternativaB;
    C.innerText = listaExercicios[num-1].alternativaC;
    D.innerText = listaExercicios[num-1].alternativaD;
    document.querySelector(".pergunta").innerText = listaExercicios[num-1].enunciado;
}
/* ATRIBUTOS DO OBJETO EXERCICIO:
idExercicio
titulo
enunciado
alternativaA
alternativaB
alternativaC
alternativaD
resposta
*/

function desabilitarAlternativas() {//função para desabilitar os botões
    alternativas.forEach((b) => b.disabled = true);//desabilita todos os botões
}

function enviarFlask(dict){
    /*
const enviarFlask = [
    {pontuacao: pontuacao},
    {sequencia: sequenciaAcerto
    }
]

//const continuar = document.getElementById("continuar");
const finalizar = document.getElementById("finalizar");

finalizar.addEventListener("click", async function() {

    const res = await fetch("/fase1/finalizar", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({pontuacao: pontuacao})
    })
    const data = await res.json();
    console.log(data);
})
*/

}