from flask import render_template

from controllers.ExercicioController import ExercicioController
from controllers.FaseController import FaseController
from app import app
@app.route('/fase')
def fase():
    oFaseController = FaseController()
    return oFaseController.fase()
        
    
# @app.route('/fase/finalizar', methods=['POST'])
# def finalizar_fase():
#     dados = request.get_json()
#     pontuacao = dados.get('pontuacao')


@app.route('/cadastrarExercicio')
def cadastrarExercicio():
    oExercicioController = ExercicioController()
    return oExercicioController.cadastrarExercicio()


@app.route('/criarExercicio', methods=['POST'])
def criarExercicio():
    oExercicioController = ExercicioController()
    return oExercicioController.criarExercicio()

@app.route('/conclusaoFase/<int:idFase>/<int:pontuacao>')
def conclusaoFase(idFase,pontuacao):
    oFaseController = FaseController()
    return oFaseController.conclusaoFase(idFase=idFase,pontuacao=pontuacao)

@app.route('/principal')
def principal():
    return render_template('principal.html')
