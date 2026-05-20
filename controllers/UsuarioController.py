from service.UsuarioService import UsuarioService
from views.UsuarioView import UsuarioView
class UsuarioController:
    def __init__(self):
        pass


    def index(self):
        oUsuarioView = UsuarioView()
        return  oUsuarioView.index()

    def cadastrar(self):
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