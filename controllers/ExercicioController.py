from service.ExercicioService import ExercicioService
from views.ExercicioView import ExercicioView
class ExercicioController:
    def __init__(self):
        pass

    def criarExercicio(self):
        oExercicioService = ExercicioService()
        return oExercicioService.criarExercicio()
    
    def cadastrarExercicio(self):
        oExercicioView = ExercicioView()
        return oExercicioView.cadastrarExercicio()