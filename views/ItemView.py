from flask import render_template

class ItemView:
    def __init__(self):
        pass

    def loja(self,listaItens,listaEstoque):
        return render_template('loja.html', listaItens=listaItens, listaEstoque=listaEstoque)
    