from controllers.ExercicioController import ExercicioController
from controllers.FaseController import FaseController
from app import app
@app.route('/fase')
def fase():
    oFaseController = FaseController()
    return oFaseController.fase()

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
