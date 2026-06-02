from service.FaseService import FaseService
from views.FaseView import FaseView
class FaseController:
    def __init__(self):
        pass
    
    def fase(self):
        oFaseService = FaseService()
        return oFaseService.fase()
    
    def conclusaoFase(self,pontuacao,idFase):
        oFaseView = FaseView()
        return oFaseView.conclusaoFase(pontuacao,idFase)