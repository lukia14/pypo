from modelsPy import Usuario,Progresso
from flask import flash, session,request
from models.UsuarioModel import UsuarioModel
from app import bd

class UsuarioDao:
    def __init__(self):
        pass

    def criarNovoUsuario(self,novo_usuario):
        bd.session.add(novo_usuario)
        bd.session.flush()
        idUsuario = novo_usuario.idUsuario

        self.criarProgresso(idUsuario)
        bd.session.commit()
        flash('Usuário cadastrado com sucesso!', 'success')
        session['usuario_logado'] = novo_usuario.nickname

    def autenticarUsuario(self,usuario):
        usuario = UsuarioModel.query.filter_by(nickname = usuario.nickname).first()
        if usuario:
            if usuario.senha == usuario.senha:
                session['usuario_logado'] = usuario.nickname
                flash('Usuário autenticado com sucesso!', 'success')
                return '/'
            else:
                flash('Erro ao autenticar. Verifique os dados e tente novamente.', 'error')
        else:
            flash('Usuário não encontrado. Verifique os dados e tente novamente.', 'error')
            return 'login'

    def criarProgresso(self,idUsuario):
        novo_progresso = Progresso(idUsuario =idUsuario, idFase=1)
        bd.session.add(novo_progresso)

    def UsuarioExiste(self,nickname):
        usuario = Usuario.query.filter_by(nickname=nickname).first()
        if usuario:
            return True
        return False