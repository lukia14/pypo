from models.FaseModel import FaseModel
from views.FaseView import FaseView
class FaseController:
    def __init__(self):
        pass
    
    def fase1(self):
        oFaseModel = FaseModel()
        return oFaseModel.fase1()
    
    def conclusaoFase(self,idFase,pontuacao):
        oFaseView = FaseView()
        oFaseView.conclusaoFase(idFase,pontuacao)