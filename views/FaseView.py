from flask import render_template,request
class FaseView:
    def __init__(self):
        pass
    
    def fase1(self,usuario,lista_dicionarios):
        return render_template('fase1.html', titulo='Fase 1', usuario=usuario, lista_exercicios=lista_dicionarios)
    
    def conclusaoFase(self,idFase,pontuacao):
        return render_template('conclusaoFase.html',idFase=idFase,pontuacao=pontuacao)
    
    