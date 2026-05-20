from app import  bd
from modelsPy import Exercicio
class ExercicioDao:
    def __init__(self):
        pass

    def criarNovoExercicio(self,exercicio):
       
        bd.session.add(exercicio)
        bd.session.commit()
    
    def exercicioExiste(self,enunciado):
        exercicio = Exercicio.query.filter_by(enunciado=enunciado).first()
        if exercicio:
            return True
        else:
            return False