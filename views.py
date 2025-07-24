from flask import render_template,flash, request, redirect, url_for, session
from main import app, bd
from helpers import FormularioUsuario
from models import Usuario

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
    if session['usuario_logado'] != None:
        flash(f'Você já está logado como {session['usuario_logado']}')
        return redirect(url_for('index'))
    
    form = FormularioUsuario(request.form)
    session['usuario_logado'] = form.nickname.data
    return render_template('login.html', form=form, titulo='Login')

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Você foi desconectado com sucesso!', 'success')
    return redirect(url_for('index'))