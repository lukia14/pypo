from app import bd
from models.FaseModel import FaseModel
class FaseDao:
    def __init__(self):
        pass

    def getFase(self,idFase):
        return FaseModel.query.filter_by(idFase=idFase).first()
