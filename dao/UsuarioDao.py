from modelsPy import Usuario,Progresso
from flask import render_template,flash, request, redirect, url_for, session
from main import bd
from views.UsuarioView import UsuarioView
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

    def criarProgresso(self,idUsuario):
        novo_progresso = Progresso(idUsuario =idUsuario, idFase=1)
        bd.session.add(novo_progresso)

    def UsuarioExiste(self,nickname):
        usuario = Usuario.query.filter_by(nickname=nickname).first()
        if usuario:
            return True
        return False