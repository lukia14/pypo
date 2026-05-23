from models.FaseModel import FaseModel
from views.FaseView import FaseView
class FaseController:
    def __init__(self):
        pass
    
    def fase(self):
        oFaseModel = FaseModel()
        return oFaseModel.fase()
    
    def conclusaoFase(self,pontuacao,idFase):
        oFaseView = FaseView()
        return oFaseView.conclusaoFase(pontuacao,idFase)