from models.EstoqueModel import EstoqueModel
from models.ItemModel import ItemModel
from app import bd

class Estoquedao:
    def __init__(self):
        pass

    def carregarEstoqueUsuario(self, idUsuario):
       
       return bd.session.query(ItemModel.nome, EstoqueModel.qtd).join(EstoqueModel, ItemModel.idItem == EstoqueModel.idItem).filter(EstoqueModel.idUsuario == idUsuario).all()
    
    def carregarEstoqueUsuarioAPI(self, idUsuario):
        return bd.session.query(ItemModel.idItem, ItemModel.nome, ItemModel.descricao, ItemModel.valor, EstoqueModel.qtd).join(EstoqueModel, ItemModel.idItem == EstoqueModel.idItem).filter(EstoqueModel.idUsuario == idUsuario).all()