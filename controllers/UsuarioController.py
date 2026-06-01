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
            flash('Você já está logado.', 'danger')
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
    
    def principal(self):
        oUsuarioService = UsuarioService()
        return oUsuarioService.principal()
    
    def configuracoes(self):
        oUsuarioService = UsuarioService()
        return oUsuarioService.configuracoes()
    
    def alterarPerfil(self):
        oUsuarioService = UsuarioService()
        return oUsuarioService.alterarPerfil()
    
    def alterarSenha(self):
        oUsuarioService = UsuarioService()
        return oUsuarioService.alterarSenha()
    
    def deletarConta(self):
        oUsuarioService = UsuarioService()
        return oUsuarioService.deletarConta()
    
    

    