from flask import render_template,flash, request, redirect, url_for, session
from main import app, bd
from helpers import FormularioUsuario
from modelsPy import Usuario,Progresso
from views.UsuarioView import UsuarioView
class UsuarioModel:
    def __init__(self):
        pass

    def criar(self):
        oUsuarioView = UsuarioView()
        form = FormularioUsuario(request.form)
        if not form.validate_on_submit():
            flash('Erro ao cadastrar usuário. Verifique os dados e tente novamente.','error')
            return redirect(url_for('cadastrar'))
        
        self.criarNovoUsuario(form)
        return oUsuarioView.index()
    
    def login(self):
        form = FormularioUsuario()
        oUsuarioView = UsuarioView()
        if 'usuario_logado' in session and session['usuario_logado'] is not None:
            flash(f'Você já está logado como {session['usuario_logado']}','danger')
            return redirect(url_for('index'))
        else:
            return oUsuarioView.login()
    
    def autenticar(self):
        form = FormularioUsuario(request.form)
        usuario = Usuario.query.filter_by(nickname = form.nickname.data).first()
        if usuario:
            if usuario.senha == form.senha.data:
                session['usuario_logado'] = usuario.nickname
                proxima_pagina = request.form['proxima']
                flash('Usuário autenticado com sucesso!', 'success')
                return redirect(proxima_pagina) or 'index'
            else:
                flash('Erro ao autenticar. Verifique os dados e tente novamente.', 'error')
        else:
            flash('Usuário não encontrado. Verifique os dados e tente novamente.', 'error')
            return redirect(url_for('login'))
        

    def logout(self):
        session['usuario_logado'] = None
        flash('Você foi desconectado com sucesso!', 'success')
        return redirect(url_for('index'))
    
    #Funções de auxilio
    
    def criarNovoUsuario(self,form):
        nickname = form.nickname.data
        email = form.email.data
        senha = form.senha.data

        usuario = Usuario.query.filter_by(nickname=nickname).first()
        if usuario:
            flash('Usuário já cadastrado', 'error')
            return render_template('cadastrar.html', form=form, titulo='Cadastro', mensagem='Usuário já cadastrado')
        
        novo_usuario = Usuario(nickname=nickname, email=email, senha=senha)
        bd.session.add(novo_usuario)
        bd.session.flush()
        idUsuario = novo_usuario.idUsuario

        self.criarProgresso(idUsuario)
        bd.session.commit()
        flash('Usuário cadastrado com sucesso!', 'success')
        session['usuario_logado'] = nickname

    def criarProgresso(self,idUsuario):
        novo_progresso = Progresso(idUsuario =idUsuario, idFase=1)
        bd.session.add(novo_progresso)