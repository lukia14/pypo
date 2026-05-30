from flask import render_template,flash, request, redirect, url_for, session
from helpers import FormularioUsuario
from views.UsuarioView import UsuarioView
from dao.ItemDao import ItemDao
from dao.UsuarioDao import UsuarioDao

class UsuarioService:
    def __init__(self):
        pass
    def criarUsuario(self):        
        oUsuarioView = UsuarioView()
        oUsuarioDao = UsuarioDao()
        form = FormularioUsuario(request.form)
        if not form.validate_on_submit():
            flash('Erro ao cadastrar usuário. Verifique os dados e tente novamente.','danger')
            return redirect(url_for('cadastrar'))
        
        if oUsuarioDao.UsuarioExiste(form):
            flash('Usuario já cadastrado','danger')
            oUsuarioView.login()
        else:
            oUsuarioDao.criarNovoUsuario(form)
        return oUsuarioView.principal()
    
    def login(self):
        form = FormularioUsuario()
        oUsuarioView = UsuarioView()
        if 'usuario_logado' in session and session['usuario_logado'] is not None:
            flash(f'Você já está logado como {session['usuario_logado']}','danger')
            return oUsuarioView.principal()
       
        return oUsuarioView.login(form)
    
    def autenticar(self):
        oUsuarioView = UsuarioView()
        oUsuarioDao = UsuarioDao()
        form = FormularioUsuario(request.form)
        usuario = oUsuarioDao.getUsuario(form)
        if usuario:
            if usuario.senha == form.senha.data and usuario.email == form.email.data:
                session['usuario_logado'] = usuario.nickname
                flash('Usuário autenticado com sucesso!', 'success')
                return oUsuarioView.principal()
            
        flash('Erro ao autenticar. Verifique os dados e tente novamente.', 'danger')
        return oUsuarioView.login(form)

    def logout(self):
        session['usuario_logado'] = None   
        flash('Você foi desconectado com sucesso!', 'success')
        return redirect(url_for('index'))
    
    def principal(self):
        oUsuarioView = UsuarioView()
        if 'usuario_logado' not in session or session['usuario_logado'] is None:
            flash('Faça login para acessar a página principal', 'danger')
            return redirect(url_for('login'))
        return oUsuarioView.principal()
    
    def loja(self):
        oItemDao = ItemDao()
        if 'usuario_logado' not in session or session['usuario_logado'] is None:
            flash('Faça login para acessar a loja', 'danger')
            return redirect(url_for('login'))
        listaItens = oItemDao.carregarItensLoja()
        oUsuarioView = UsuarioView()
        return oUsuarioView.loja(listaItens)
    
    #Funções de auxilio
    
   