from flask import render_template, request, redirect, session, flash, url_for
from main import app, bd
from helpers import FormularioExercicio
from modelsPy import Exercicio,Progresso,Usuario,Fase

class ExercicioModel:
    def __init__(self):
        pass
    
    def criarExercicio(self):
        form = FormularioExercicio(request.form)
        if not form.validate_on_submit():
            flash('Erro ao criar exercício. Verifique os dados e tente novamente.','error')
            return redirect(url_for('cadastrarExercicio'))
        
        novo_exercicio = self.criar_exercicio(form)
        if not novo_exercicio: # Verifica se o exercício já existe
            flash('Erro: Exercício com esse ID já existe.', 'error')
            return redirect(url_for('cadastrarExercicio'))
        
        flash('Exercício criado com sucesso!', 'success')
        return redirect(url_for('index')) 
    
    #Funções Auxiliares
    def criar_exercicio(form):
        idExercicio = form.idExercicio.data
        numero = form.numero.data
        titulo = form.titulo.data
        enunciado = form.enunciado.data
        alternativaA = form.alternativaA.data
        alternativaB = form.alternativaB.data
        alternativaC = form.alternativaC.data
        alternativaD = form.alternativaD.data
        resposta = form.resposta.data
        exercicio = Exercicio.query.filter_by(idExercicio=idExercicio).first()
        if exercicio:
            return None  # Exercicio já existe, não criar duplicado
        novo_exercicio = Exercicio(idExercicio=idExercicio, numero=numero, titulo=titulo, enunciado=enunciado, alternativaA=alternativaA, alternativaB=alternativaB, alternativaC=alternativaC, alternativaD=alternativaD, resposta=resposta)
        bd.session.add(novo_exercicio)
        bd.session.commit()
        return novo_exercicio