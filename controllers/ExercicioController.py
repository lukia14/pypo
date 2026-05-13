from models.ExercicioModel import ExercicioModel
from views.ExercicioView import ExercicioView
class ExercicioController:
    def __init__(self):
        pass

    def criarExercicio(self):
        oExercicioModel = ExercicioModel()
        return oExercicioModel.criarExercicio()
    
    def cadastrarExercicio(self):
        oExercicioView = ExercicioView()
        return oExercicioView.cadastrarExercicio()