from flask import flash, redirect, session, url_for,jsonify,request
from views.ItemView import ItemView
from dao.EstoqueDao import Estoquedao
from dao.ItemDao import ItemDao
from dao.UsuarioDao import UsuarioDao
class ItemService:
    def __init__(self):
        pass

    def loja(self):
            idUsuario = session['usuario_logado']
            oItemDao = ItemDao()
            oEstoqueDao = Estoquedao()
            oUsuarioDao = UsuarioDao()
            pontuacao = oUsuarioDao.getPontuacao(idUsuario)
            if not self.verificarLogin():
                flash('Faça login para acessar a loja', 'danger')
                return redirect(url_for('login'))
            listaItens = oItemDao.carregarItensLoja()
            listaEstoque = oEstoqueDao.carregarEstoqueUsuario(idUsuario)              
            oItemView = ItemView()
            return oItemView.loja(listaItens, listaEstoque,pontuacao)

    def apiItensLoja(self):
        oItemDao = ItemDao()
        listaItens = oItemDao.carregarItensLoja()
        listaParaJS =[]
        for item in listaItens:
            listaParaJS.append({
                'idItem': item.idItem,
                'nome': item.nome,
                'descricao': item.descricao,
                'valor': item.valor
            })
        return jsonify(listaParaJS)
    
    def apiEstoque(self):
        oEstoqueDao = Estoquedao()
        listaEstoque = oEstoqueDao.carregarEstoqueUsuarioAPI(session['usuario_logado'])
        listaParaJS = []
        for item in listaEstoque:
            listaParaJS.append({
                'idItem': item.idItem,
                'nome': item.nome,
                'descricao': item.descricao,
                'valor': item.valor,
                'qtd': item.qtd  
            })
        return jsonify(listaParaJS)
    
    def apiSalvarCompra(self):
        oEstoqueDao = Estoquedao()
        oUsuarioDao = UsuarioDao()
        dados = request.get_json(silent=True)
        if not dados:
            return jsonify({'status': 'erro', 'mensagem': 'Dados de compra não fornecidos'}), 400
    
        listaEstoqueEnviada = dados.get('estoque')     
        novaPontuacao = dados.get('pontuacao')          
        oUsuarioDao.setPontuacao(session['usuario_logado'],novaPontuacao)
        if listaEstoqueEnviada:
            for item in listaEstoqueEnviada:
                idItem= item.get('idItem')
                qtd= item.get('qtd')
                oEstoqueDao.adicionarAoEstoque(session['usuario_logado'],idItem,qtd)
        return {"status": "sucesso", "mensagem": "Compra salva com sucesso!"}, 200
    
    #funções auxiliares
    def verificarLogin(self):
        if 'usuario_logado' not in session or session['usuario_logado'] is None:
            flash('Faça login para acessar esta página', 'danger')
            return False
        return True