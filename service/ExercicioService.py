from flask import render_template, request, redirect, session, flash, url_for
from helpers import FormularioExercicio
from modelsPy import Exercicio,Progresso,Usuario,Fase
from views.ExercicioView import ExercicioView
from dao.ExercicioDao import ExercicioDao

class ExercicioService:
    def __init__(self):
        pass

    def criarExercicio(self):
        oExercicioView = ExercicioView()
        oExercicioDao = ExercicioDao()
        form = FormularioExercicio(request.form)
        if not form.validate_on_submit():
            flash('Erro ao criar exercício. Verifique os dados e tente novamente.','error')
            return redirect(oExercicioView.cadastrarExercicio())
        exercicio = self.modeloExercicio(form)
        if oExercicioDao.exercicioExiste(exercicio.enunciado):
            return redirect(oExercicioView.cadastrarExercicio())
        else:
            oExercicioDao.criarNovoExercicio(exercicio)
        
        flash('Exercício criado com sucesso!', 'success')
        return redirect(url_for('index')) 