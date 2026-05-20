from app import app
from controllers.UsuarioController import UsuarioController

@app.route('/')
def index():
    oUsuarioController = UsuarioController()
    return  oUsuarioController.index()


@app.route('/cadastrar')
def cadastrar():
    oUsuarioController = UsuarioController()
    return  oUsuarioController.cadastrar()

@app.route('/criar', methods=['POST'])
def criar():
    oUsuarioController = UsuarioController()
    return oUsuarioController.criar()

@app.route('/login')
def login():
    oUsuarioController = UsuarioController()
    return oUsuarioController.login()
    

@app.route('/autenticar', methods=['POST'])
def autenticar():
    oUsuarioController = UsuarioController()
    return oUsuarioController.autenticar()

@app.route('/logout')
def logout():
    oUsuarioController = UsuarioController()
    return oUsuarioController.logout()



