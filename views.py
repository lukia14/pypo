from flask import render_template,flash, request, redirect, url_for, session
from main import app, bd
from helpers import FormularioUsuario, FormularioExercicio
from models import Usuario, Exercicio

@app.route('/')
def index():
    return render_template('index.html',titulo='PaginaInicial')


@app.route('/cadastrar')
def cadastrar():
    form = FormularioUsuario()
    return render_template('cadastrar.html', form=form, titulo='Cadastro')

@app.route('/criar', methods=['POST'])
def criar():
    form = FormularioUsuario(request.form)
    if not form.validate_on_submit():
        flash('Erro ao cadastrar usuário. Verifique os dados e tente novamente.','error')
        return redirect(url_for('cadastrar'))
    
    nickname = form.nickname.data
    email = form.email.data
    senha = form.senha.data

    usuario = Usuario.query.filter_by(nickname=nickname).first()
    if usuario:
        flash('Usuário já cadastrado', 'error')
        return render_template('cadastrar.html', form=form, titulo='Cadastro', mensagem='Usuário já cadastrado')
    
    novo_usuario = Usuario(nickname=nickname, email=email, senha=senha)
    bd.session.add(novo_usuario)
    bd.session.commit()
    flash('Usuário cadastrado com sucesso!', 'success')
    session['usuario_logado'] = nickname
    return redirect(url_for('index'))

@app.route('/login')
def login():
    form = FormularioUsuario()
    if 'usuario_logado' in session:
        if session['usuario_logado'] != None:
            flash(f'Você já está logado como {session['usuario_logado']}')
            return redirect(url_for('index'))
    else:
        proxima = request.args.get('proxima')
        return render_template('login.html', titulo='Login', form=form, proxima = proxima)

@app.route('/autenticar', methods=['POST'])
def autenticar():
    form = FormularioUsuario(request.form)
    usuario = Usuario.query.filter_by(nickname = form.nickname.data).first()
    if usuario:
        if usuario.senha == form.senha.data:
            session['usuario_logado'] = usuario.nickname
            proxima_pagina = request.form['proxima']
            flash('Usuário autenticado com sucesso!', 'success')
            return redirect(url_for(proxima_pagina))
        else:
            flash('Erro ao autenticar. Verifique os dados e tente novamente.', 'error')
    else:
        flash('Usuário não encontrado. Verifique os dados e tente novamente.', 'error')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Você foi desconectado com sucesso!', 'success')
    return redirect(url_for('index'))

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