from flask import render_template,request
from helpers import FormularioExercicio
class ExercicioView:
    def __init__(self):
        pass
    def cadastrarExercicio(self):
        form = FormularioExercicio()
        return render_template('cadastrarExercicio.html', form=form, titulo='Criar Exercício')