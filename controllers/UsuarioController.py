from models.UsuarioModel import UsuarioModel
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
        oUsuarioModel = UsuarioModel()
        return oUsuarioModel.criarUsuario()
    
    def login(self):
        oUsuarioModel = UsuarioModel()
        return oUsuarioModel.login()

    def autenticar(self):
        oUsuarioModel = UsuarioModel()
        return oUsuarioModel.autenticar()
    
    def logout(self):
        oUsuarioModel = UsuarioModel()
        return oUsuarioModel.logout()