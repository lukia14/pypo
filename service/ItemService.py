from flask import flash, redirect, session, url_for,jsonify
from views.ItemView import ItemView
from dao.ItemDao import ItemDao
class ItemService:
    def __init__(self):
        pass

    def loja(self):
            oItemDao = ItemDao()
            if not self.verificarLogin():
                flash('Faça login para acessar a loja', 'danger')
                return redirect(url_for('login'))
            listaItens = oItemDao.carregarItensLoja()
            oItemView = ItemView()
            return oItemView.loja(listaItens)
    
    def apiItensLoja(self):
        oItemDao = ItemDao()
        listaItens = oItemDao.carregarItensLoja()
        listaParaJS =[]
        for item in listaItens:
            listaParaJS.append({
                'id': item.id,
                'nome': item.nome,
                'descricao': item.descricao,
                'valor': item.valor
            })
        return jsonify(listaParaJS)
    
    
    #funções auxiliares
    def verificarLogin(self):
        if 'usuario_logado' not in session or session['usuario_logado'] is None:
            flash('Faça login para acessar esta página', 'danger')
            return False
        return True