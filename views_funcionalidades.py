from app import app
from controllers.UsuarioController import UsuarioController
from controllers.ItemController import ItemController


@app.route('/principal')
def principal():
    oUsuarioController = UsuarioController()
    return oUsuarioController.principal()

@app.route('/configuracoes')
def configuracoes():
    oUsuarioController = UsuarioController()
    return oUsuarioController.configuracoes()

@app.route('/loja')
def loja():
    oItemController = ItemController()
    return oItemController.loja()

@app.route('/api/itensLoja')
def apiItensLoja():
    oItemController = ItemController()
    return oItemController.apiItensLoja()