const botoes = document.querySelectorAll('.botao-comprar')
const pontuacaoHTML = document.getElementById('pontuacao')
const botaoSalvarCompra = document.querySelector('.botao-sair-salvar')
var pontuacao = parseInt(pontuacaoHTML.textContent.split(' ')[1])

botaoSalvarCompra.addEventListener('click', () => {
    console.log('Salvando compra...')
    const tokencsrf = document.querySelector('meta[name="csrf-token"]').getAttribute('content');
    fetch('/api/salvarCompra',{
        method: 'POST',
        headers:{
            'Content-Type': 'application/json',
            'X-CSRFToken': tokencsrf
        },
        body: JSON.stringify({
            'estoque': listaEstoque,
            'pontuacao': pontuacao
        })
    })
})

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

botoes.forEach(botao =>{
    botao.addEventListener('click', async (event) => {
        const itemId = event.target.classList[1]
        let item = listaItens.find(item => item.idItem == itemId)
        let valor = item?.valor || 0
        if (pontuacao < valor){
            flash(`Você precisa de ${valor} pontos, mas só tem ${pontuacao}!`, 'alerta');
            return 
        }
        pontuacao -= valor
        pontuacaoHTML.textContent = `pontuação: ${pontuacao}`
        salvarCompra(itemId)
            
    })
})

    

function salvarCompra(itemId) {
    const item = listaEstoque.find(item => item.idItem == itemId)
    if (item){
        item.qtd += 1
    }
    else{
        listaEstoque.push({idItem: itemId, qtd: 1})
    }
    renderizarEstoque()
}

function renderizarEstoque(){
    listaEstoque.forEach(item=>{
        const div = document.querySelector('.item-inventario')
        div.innerHTML = ''
        const spanNome = document.createElement('span')
        const spanQtd = document.createElement('span')
        
        spanNome.classList.add('nome-item-inventario')
        spanQtd.classList.add('qtd-item-inventario')
        
        spanNome.innerHTML = item.nome 
        spanQtd.innerHTML = item.qtd
        div.append(spanNome,spanQtd)
    })
}




function flash(mensagem, tipo = 'sucesso') {
    // Procura o container na tela
    let container = document.getElementById('flash-container');
    
    // Se o container não existir no HTML, o JS cria ele sozinho agora:
    if (!container) {
        container = document.createElement('div');
        container.id = 'flash-container';
        document.body.appendChild(container);
    }
    
    // Cria o elemento da mensagem
    const div = document.createElement('div');
    div.classList.add('flash-message', `flash-${tipo}`);
    div.innerText = mensagem;
    
    // Adiciona na tela
    container.appendChild(div);
    
    // Remove automaticamente após 4 segundos
    setTimeout(() => {
        div.remove();
    }, 4000);
}