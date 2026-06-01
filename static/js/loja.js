let botoes = document.querySelectorAll('.botao-comprar')
async function carregarItens() {
    try{
        const response = await fetch('/api/itensLoja')
        return await response.json()
        
    }catch(error){
        console.error('Erro ao carregar itens da loja:', error)
    }
}

async function carregarEstoque() {
    try{
        const response = await fetch('/api/estoque')
        return await response.json()
    }  catch(error){
        console.error('Erro ao carregar estoque:', error)
    }
}

let listaItens = await carregarItens()
let listaEstoque = await carregarEstoque()
console.log('Itens da Loja:', listaItens)
console.log('Estoque do Usuário:', listaEstoque)
botoes.forEach(botao =>{
    botao.addEventListener('click', async (event) => {
        const itemId = event.target.classList[1]
        custoTotal = listaItens.find(item => item.idItem === itemId)?.valor || 0
    })
})

    


