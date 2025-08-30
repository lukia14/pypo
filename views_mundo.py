from flask import render_template, request, redirect, session, flash, url_for
from main import app, bd
from helpers import FormularioExercicio
from models import Exercicio,Progresso,Usuario,Fase

@app.route('/fase1')
def fase1():
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        flash('Você precisa estar logado para acessar essa página.', 'error')
        return redirect(url_for('login', proxima=url_for('fase1')))
    else:
        usuario = session['usuario_logado']
        usuario_bd = Usuario.query.filter_by(nickname=usuario).first()
        idUsuario = usuario_bd.idUsuario
        progresso = Progresso.query.filter_by(idUsuario=idUsuario).order_by(Progresso.idFase.desc()).first()
        fase_atual = Fase.query.filter_by(idFase=progresso.idFase).first()
        lista_exercicios = fase_atual.exercicio
        lista_dicionarios = []
        for exercicio in lista_exercicios:
            dict_exercicio = {
                'idExercicio': exercicio.idExercicio,
                'titulo': exercicio.titulo,
                'enunciado': exercicio.enunciado,
                'alternativaA': exercicio.alternativaA,
                'alternativaB': exercicio.alternativaB,
                'alternativaC': exercicio.alternativaC,
                'alternativaD': exercicio.alternativaD,
                'resposta': exercicio.resposta
            }
            lista_dicionarios.append(dict_exercicio)

        return render_template('fase1.html', titulo='Fase 1', usuario=usuario, lista_exercicios=lista_dicionarios)

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
    
    novo_exercicio = criar_exercicio(form)
    if not novo_exercicio: # Verifica se o exercício já existe
        flash('Erro: Exercício com esse ID já existe.', 'error')
        return redirect(url_for('cadastrarExercicio'))
    
    flash('Exercício criado com sucesso!', 'success')
    return redirect(url_for('index')) 


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