from app import bd
class ExercicioModel(bd.Model):
    __tablename__ = 'Exercicio'
    idExercicio = bd.Column(bd.Integer, primary_key=True, autoincrement=True)
    titulo = bd.Column(bd.String(25), nullable=False)
    enunciado = bd.Column(bd.String(99), nullable=False)
    alternativaA = bd.Column(bd.String(99), nullable=False)
    alternativaB = bd.Column(bd.String(99), nullable=False)
    alternativaC = bd.Column(bd.String(99), nullable=False)
    alternativaD = bd.Column(bd.String(99), nullable=False)
    resposta = bd.Column(bd.String(1), nullable=False)
    idFase = bd.Column(bd.Integer, bd.ForeignKey('fase.idFase'))
    numero = bd.Column(bd.Integer, nullable=False)

    def __repr__(self):
        return'<Exercicio %r>' % self.titulo
    
    
    
    #Funções Auxiliares
    def modeloExercicio(self,form):
        numero = form.get('numero')
        titulo = form.get('titulo')
        enunciado = form.get('enunciado')
        alternativaA = form.get('alternativaA')
        alternativaB = form.get('alternativaB')
        alternativaC = form.get('alternativaC')
        alternativaD = form.get('alternativaD')
        resposta = form.get('resposta')
        novo_exercicio = ExercicioModel(numero=numero,enunciado=enunciado,titulo=titulo,alternativaA=alternativaA,alternativaB=alternativaB,alternativaC=alternativaC,alternativaD=alternativaD,resposta=resposta)
        return novo_exercicio