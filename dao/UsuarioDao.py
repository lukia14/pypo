from modelsPy import Usuario,Progresso
from flask import flash, session,request
from models.UsuarioModel import UsuarioModel
from models.ItemModel import ItemModel
from app import bd

class UsuarioDao:
    def __init__(self):
        pass

    def getUsuario(self,form):
        usuario = UsuarioModel.query.filter_by(nickname=form.nickname.data).first()
        return usuario

    def getUsuarioPorNickname(self, nickname):
        usuario = UsuarioModel.query.filter_by(nickname=nickname).first()
        return usuario

    def criarNovoUsuario(self,form):
        novo_usuario = UsuarioModel.modeloUsuario(form)
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

    def alterarPerfil(self,form):
        usuarioAntigo = UsuarioModel.query.filter_by(nickname=session['usuario_logado']).first()
        if usuarioAntigo:
            usuarioAntigo.email = form.email.data
            bd.session.commit()
            flash('Perfil atualizado com sucesso!', 'success')
            return True
        else:
            flash('Usuário não encontrado. Verifique os dados e tente novamente.', 'error')
            return False
        
    def alterarSenha(self,form):
        usuarioAntigo = UsuarioModel.query.filter_by(nickname=session['usuario_logado']).first()
        senhaAntiga = usuarioAntigo.senha if usuarioAntigo else None
        if not senhaAntiga:
            flash('Usuário não encontrado. Verifique os dados e tente novamente.', 'error')

        if senhaAntiga != form.senhaAntiga.data:
            flash('Senha antiga incorreta. Verifique os dados e tente novamente.', 'error')

        if form.novaSenha.data != form.confirmarSenha.data:
            flash('As novas senhas não coincidem. Verifique os dados e tente novamente.', 'error')
            
        flash('Senha alterada com sucesso!', 'success')
        usuarioAntigo.senha = form.novaSenha.data
        bd.session.commit()
        
    def deletarConta(self, nickname):
        usuario = UsuarioModel.query.filter_by(nickname=nickname).first()
        if usuario:
            bd.session.delete(usuario)
            bd.session.commit()
            flash('Conta deletada com sucesso!', 'success')

    #funções de auxilio
    
    def UsuarioExiste(self,form):
        usuario = Usuario.query.filter_by(nickname=form.nickname.data).first()
        if usuario:
            return True
        return False