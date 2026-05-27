from flask import render_template,request
from helpers import FormularioExercicio
class ExercicioView:
    def __init__(self):
        pass
    def cadastrarExercicio(self, idExercicio):
        form = FormularioExercicio(idExercicio=idExercicio)
        return render_template('cadastrarExercicio.html', form=form, titulo='Criar Exercício')
    
    def listarExercicios(self, listaExercicios):
        return render_template('listarExercicios.html', listaExercicios=listaExercicios, titulo='Lista de Exercícios')