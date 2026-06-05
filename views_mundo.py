from app import app
from controllers.ExercicioController import ExercicioController
from controllers.FaseController import FaseController
from controllers.ModuloController import ModuloController
@app.route('/modulo')
def modulo():
    oModuloController = ModuloController()
    return oModuloController.modulo()

@app.route('/fase/<int:idFase>')
def fase(idFase):
    oFaseController = FaseController()
    return oFaseController.fase(idFase)

@app.route('/conclusaoFase/<int:idFase>/<int:pontuacao>')
def conclusaoFase(idFase,pontuacao):
    oFaseController = FaseController()
    return oFaseController.conclusaoFase(idFase=idFase,pontuacao=pontuacao)

# Exercicio
@app.route('/cadastrarExercicio')
def cadastrarExercicio():
    oExercicioController = ExercicioController()
    return oExercicioController.cadastrarExercicio()


@app.route('/criarExercicio', methods=['POST'])
def criarExercicio():
    oExercicioController = ExercicioController()
    return oExercicioController.criarExercicio()
@app.route('/listarExercicios')
def listarExercicios():
    oExercicioController = ExercicioController()
    return oExercicioController.listarExercicios()

@app.route('/exercicio/editar/<int:idExercicio>')
def editarExercicio(idExercicio):
    oExercicioController = ExercicioController()
    return oExercicioController.editarExercicio(idExercicio)

@app.route('/exercicio/alterar',methods=['POST'])
def alterarExercicio():
    oExercicioController = ExercicioController()
    return oExercicioController.alterarExercicio()

@app.route('/exercicio/deletar/<int:idExercicio>')
def deletarExercicio(idExercicio):
    oExercicioController = ExercicioController()
    return oExercicioController.deletarExercicio(idExercicio)

#Fase
@app.route('/listarFases')
def listarFases():
    from flask import render_template
    return render_template('listarFases.html')
#Modulo
@app.route('/listarModulos')
def listarModulos():
    from flask import render_template
    return render_template('listarModulos.html')

#Mundo
@app.route('/listarMundos')
def listarMundos():
    from flask import render_template
    return render_template('listarMundos.html')

#Itens
@app.route('/listarItens')
def listarItens():
    from flask import render_template
    return render_template('listarItens.html')