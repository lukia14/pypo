from flask import flash, redirect, session, url_for
from service.UsuarioService import UsuarioService
from views.UsuarioView import UsuarioView
class UsuarioController:
    def __init__(self):
        pass


    def index(self):
        oUsuarioView = UsuarioView()
        return  oUsuarioView.index()

    def cadastrar(self):
        if 'usuario_logado' in session and session['usuario_logado'] is not None:
            flash(f'Você já está logado como {session['usuario_logado']}','danger')
            return redirect(url_for('index'))   
        oUsuarioView = UsuarioView()
        return  oUsuarioView.cadastrar()
    
    def criar(self):
        oUsuarioService = UsuarioService()
        return oUsuarioService.criarUsuario()
    
    def login(self):
        oUsuarioService = UsuarioService()
        return oUsuarioService.login()

    def autenticar(self):
        oUsuarioService = UsuarioService()
        return oUsuarioService.autenticar()

    def logout(self):
        oUsuarioService = UsuarioService()
        return oUsuarioService.logout()