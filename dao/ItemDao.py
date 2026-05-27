from models.ItemModel import ItemModel
from flask import jsonify
class ItemDao:
    def __init__(self):
        pass

    def carregarItensLoja(self):
        listaItens = ItemModel.query.all()
        return listaItens