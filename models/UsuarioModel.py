from flask import render_template,flash, request, redirect, url_for, session
from main import bd
from helpers import FormularioUsuario
from modelsPy import Usuario,Progresso
from views.UsuarioView import UsuarioView
from dao.UsuarioDao import UsuarioDao
class UsuarioModel:
    def __init__(self):
        pass

    def criarUsuario(self):
        oUsuarioView = UsuarioView()
        form = FormularioUsuario(request.form)
        if not form.validate_on_submit():
            flash('Erro ao cadastrar usuário. Verifique os dados e tente novamente.','error')
            return redirect(url_for('cadastrar'))
        
        oUsuarioDao = UsuarioDao()

        usuario = self.modeloUsuario(form)
        if oUsuarioDao.UsuarioExiste(usuario.nickname):
            flash('Usuario já cadastrado','danger')
            oUsuarioView.login()
        else:
            oUsuarioDao.criarNovoUsuario(usuario)
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
    
    def modeloUsuario(self,form):
        nickname = form.nickname.data
        email = form.email.data
        senha = form.senha.data
        usuario = Usuario(nickname=nickname, email=email, senha=senha)
        return usuario