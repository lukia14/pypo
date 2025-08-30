from flask import render_template,flash, request, redirect, url_for, session
from main import app, bd
from helpers import FormularioUsuario
from models import Usuario,Progresso

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
    idUsuario = novo_usuario.idUsuario
    novo_progresso = Progresso(idUsuario =idUsuario, idFase=1)
    bd.session.add(novo_progresso)
    bd.session.commit()


    flash('Usuário cadastrado com sucesso!', 'success')
    session['usuario_logado'] = nickname
    return redirect(url_for('index'))

@app.route('/login')
def login():
    form = FormularioUsuario()
    if 'usuario_logado' in session and session['usuario_logado'] is not None:
        flash(f'Você já está logado como {session['usuario_logado']}','danger')
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