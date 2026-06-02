from flask import redirect, session, flash, url_for
from app import app, bd
from dao.UsuarioDao import UsuarioDao
from dao.ProgressoDao import ProgressoDao
from dao.FaseDao import FaseDao
from helpers import FormularioExercicio
from views.FaseView import FaseView

class FaseService:
    def __init__(self):
        pass
    def fase(self):
        idUsuario = session['usuario_logado']
        oFaseView = FaseView()
        oProgressoDao = ProgressoDao()
        oFaseDao = FaseDao()
        if not self.verificarLogin():
            flash('Você precisa estar logado para acessar essa página.', 'error')
            return redirect(url_for('login', proxima=url_for('fase')))
        else:
            progresso = oProgressoDao.getProgresso(idUsuario)
            fase = oFaseDao.getFase(progresso.idFase)
            lista_exercicios = fase.exercicio

            lista_dicionarios = self.criar_lista_exercicios_dict(lista_exercicios)# Converte a lista de exercícios em uma lista de dicionários
            return oFaseView.fase(idUsuario,lista_dicionarios, fase.idFase)
            
        
    #funções auxiliares
    def criar_lista_exercicios_dict(self,lista_exercicios):
        lista_dicionarios = []
        for exercicio in lista_exercicios:
            dict_exercicio = {
                'idExercicio': exercicio.idExercicio,
                'titulo': exercicio.titulo,
                'enunciado': exercicio.enunciado,
                'alternativaA': exercicio.alternativaA,
                'alternativaB': exercicio.alternativaB,
                'alternativaC': exercicio.alternativaC,
                'alternativaD': exercicio.alternativaD,
                'resposta': exercicio.resposta
            }
            lista_dicionarios.append(dict_exercicio)
        return lista_dicionarios
    
    #funções auxiliares
    def verificarLogin(self):
        if 'usuario_logado' not in session or session['usuario_logado'] is None:
            flash('Faça login para acessar esta página', 'danger')
            return False
        return True