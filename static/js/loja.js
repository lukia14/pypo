let botao = document.querySelectorAll('.botao-comprar')
async function carregarItens() {
    try{
        const response = await fetch('/api/itensLoja')
        return await response.json()
        
    }catch(error){
        console.error('Erro ao carregar itens da loja:', error)
    }
}
console.log(await carregarItens())

