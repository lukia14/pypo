const botao1 = document.createElement("button")
const botao2 = document.createElement("button")
const botao3 = document.createElement("button")
const botao4 = document.createElement("button")
const div = document.querySelector(".botoes")
const balao = document.querySelector('.balao')
const contaudo_balao = document.querySelector('.conteudo-dica')
contaudo_balao.innerHTML = 'dica'

botao1.innerHTML = "my_var"
botao2.innerHTML = "2_variable"
botao3.innerHTML = "Variable name"
botao4.innerHTML = "Var!"

botao1.classList.add('botao')
botao2.classList.add('botao')
botao3.classList.add('botao')
botao4.classList.add('botao')

botao1.addEventListener("click", () => {
    botao1.classList.add("acerto")
    botao2.remove()
    botao3.remove()
    botao4.remove()
})
botao2.addEventListener("click", () => {
    botao2.classList.add("erro")
})

botao3.addEventListener("click", () => {
    botao3.classList.add("erro")
})

botao4.addEventListener("click", () => {
    botao4.classList.add("erro")
})

div.append(botao1, botao2, botao3, botao4)


balao.addEventListener('click',()=>{
    contaudo_balao.innerHTML = 'Dica: Variáveis não podem começar com número, ter espaço ou símbolo!'

})
