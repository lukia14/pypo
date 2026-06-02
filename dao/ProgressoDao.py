from app import bd
from models.ProgressoModel import ProgressoModel

class ProgressoDao:
    def __init__(self):
        pass

    def getProgresso(self,idUsuario):
        return ProgressoModel.query.filter_by(idUsuario=idUsuario).first()
        
    
    def criarProgresso(self,idUsuario):
        novoProgresso = ProgressoModel(idUsuario =idUsuario, idFase=1)
        bd.session.add(novoProgresso)