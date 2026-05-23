from flask import render_template, request, redirect, session, flash, url_for
from app import app, bd
from helpers import FormularioExercicio
from modelsPy import Exercicio,Progresso,Usuario,Fase
from views.FaseView import FaseView
class FaseModel:
    def __init__(self):
        pass
    def fase(self):
        oFaseView = FaseView()
        if 'usuario_logado' not in session or session['usuario_logado'] is None:
            flash('Você precisa estar logado para acessar essa página.', 'error')
            return redirect(url_for('login', proxima=url_for('fase')))
        else:
            usuario = session['usuario_logado']
            usuario_bd = Usuario.query.filter_by(nickname=usuario).first()
            idUsuario = usuario_bd.idUsuario
            progresso = Progresso.query.filter_by(idUsuario=idUsuario).order_by(Progresso.idFase.desc()).first()
            fase_atual = Fase.query.filter_by(idFase=progresso.idFase).first()
            lista_exercicios = fase_atual.exercicio

            lista_dicionarios = self.criar_lista_exercicios_dict(lista_exercicios)# Converte a lista de exercícios em uma lista de dicionários
            return oFaseView.fase(usuario,lista_dicionarios, progresso.idFase)
            
        
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