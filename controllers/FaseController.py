from service.FaseService import FaseService
from views.FaseView import FaseView
class FaseController:
    def __init__(self):
        pass
    
    def fase(self,idFase):
        oFaseService = FaseService()
        return oFaseService.fase(idFase)
    
    def conclusaoFase(self,pontuacao,idFase):
        oFaseView = FaseView()
        return oFaseView.conclusaoFase(pontuacao,idFase)