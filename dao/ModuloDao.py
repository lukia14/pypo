from database import bd
from models.ModuloModel import ModuloModel
class ModuloDao:
    def __init__(self):
        pass
    def getModulo(self,idModulo):
        modulo =ModuloModel.query.filter_by(idModulo=idModulo).first()
        if modulo:
            return modulo
        else:
            return None