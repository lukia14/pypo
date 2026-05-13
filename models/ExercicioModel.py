from flask import render_template, request, redirect, session, flash, url_for
from helpers import FormularioExercicio
from modelsPy import Exercicio,Progresso,Usuario,Fase
from views.ExercicioView import ExercicioView
from dao.ExercicioDao import ExercicioDao

class ExercicioModel:
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
        
        if not novo_exercicio: # Verifica se o exercício já existe
            flash('Erro: Exercício com esse ID já existe.', 'error')
            return redirect(url_for('cadastrarExercicio'))
        
        flash('Exercício criado com sucesso!', 'success')
        return redirect(url_for('index')) 
    
    #Funções Auxiliares
    def modeloExercicio(self,form):
        numero = form.numero.data
        titulo = form.titulo.data
        enunciado = form.enunciado.data
        alternativaA = form.alternativaA.data
        alternativaB = form.alternativaB.data
        alternativaC = form.alternativaC.data
        alternativaD = form.alternativaD.data
        resposta = form.resposta.data
        novo_exercicio = Exercicio(numero=numero,enunciado=enunciado,titulo=titulo,alternativaA=alternativaA,alternativaB=alternativaB,alternativaC=alternativaC,alternativaD=alternativaD)
        return novo_exercicio
        # if exercicio:
        #     return None  # Exercicio já existe, não criar duplicado
        # novo_exercicio = Exercicio(idExercicio=idExercicio, numero=numero, titulo=titulo, enunciado=enunciado, alternativaA=alternativaA, alternativaB=alternativaB, alternativaC=alternativaC, alternativaD=alternativaD, resposta=resposta)
        # bd.session.add(novo_exercicio)
        # bd.session.commit()
        # return novo_exercicio