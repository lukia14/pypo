from controllers.ExercicioController import ExercicioController
from controllers.FaseController import FaseController
from main import app
@app.route('/fase1')
def fase1():
    oFaseController = FaseController()
    return oFaseController.fase1()
        
    
# @app.route('/fase1/finalizar', methods=['POST'])
# def finalizar_fase1():
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



