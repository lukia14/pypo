from flask import render_template,flash, request, redirect, url_for, session
from helpers import FormularioUsuario
from views.UsuarioView import UsuarioView
from models.UsuarioModel import UsuarioModel
from dao.UsuarioDao import UsuarioDao
class UsuarioService:
    def __init__(self):
        pass
    def criarUsuario(self):        
        oUsuarioView = UsuarioView()
        form = FormularioUsuario(request.form)
        if not form.validate_on_submit():
            flash('Erro ao cadastrar usuário. Verifique os dados e tente novamente.','danger')
            return redirect(url_for('cadastrar'))
        
        oUsuarioDao = UsuarioDao()
        oUsuarioModel = UsuarioModel()
        usuario = oUsuarioModel.modeloUsuario(form.data)
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
            return oUsuarioView.login(form)
    
    def autenticar(self):
        oUsuarioDao = UsuarioDao()
        oUsuarioModel = UsuarioModel()
        usuario = oUsuarioModel.modeloUsuario(request.form)
        return redirect(oUsuarioDao.autenticarUsuario(usuario))

    def logout(self):
        session['usuario_logado'] = None
        flash('Você foi desconectado com sucesso!', 'success')
        return redirect(url_for('index'))
    
    #Funções de auxilio
    
   