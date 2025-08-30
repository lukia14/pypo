from flask import render_template, request, redirect, session, flash, url_for
from main import app, bd
from helpers import FormularioExercicio
from models import Exercicio

@app.route('/fase1')
def fase1():
    return render_template('fase1.html', titulo='Fase 1')

@app.route('/cadastrarExercicio')
def cadastrarExercicio():
    form = FormularioExercicio()
    return render_template('cadastrarExercicio.html', form=form, titulo='Criar Exercício')


@app.route('/criarExercicio', methods=['POST'])
def criarExercicio():
    form = FormularioExercicio(request.form)
    if not form.validate_on_submit():
        flash('Erro ao criar exercício. Verifique os dados e tente novamente.','error')
        return redirect(url_for('cadastrarExercicio'))
    
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
        flash('Exercício já cadastrado', 'error')
        return render_template('cadastrarExercicio.html', form=form, titulo='Criar Exercício', mensagem='Exercício já cadastrado')
    novo_exercicio = Exercicio(idExercicio=idExercicio, numero=numero, titulo=titulo, enunciado=enunciado, alternativaA=alternativaA, alternativaB=alternativaB, alternativaC=alternativaC, alternativaD=alternativaD, resposta=resposta)
    bd.session.add(novo_exercicio)
    bd.session.commit()
    flash('Exercício criado com sucesso!', 'success')
    return redirect(url_for('index.html'))