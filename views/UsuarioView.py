from flask import render_template,request
from helpers import FormularioUsuario

class UsuarioView:
    def __init__(self):
        pass
    
    def index(self):
        return render_template('index.html',titulo='PaginaInicial')
    
    def cadastrar(self):
        form = FormularioUsuario()
        return render_template('cadastrar.html', form=form, titulo='Cadastro')
    
    def cadastroExistente(self):
        form = FormularioUsuario()
        return render_template('cadastrar.html', form=form, titulo='Cadastro',mensagem='Usuario j')
    
    def login(self):
        form = FormularioUsuario()
        proxima = request.args.get('proxima')
        return render_template('login.html', titulo='Login', form=form, proxima = proxima)
