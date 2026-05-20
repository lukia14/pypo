from app import bd

class Usuario(bd.Model):
    idUsuario = bd.Column(bd.Integer, primary_key=True, autoincrement=True)
    nickname = bd.Column(bd.String(25), nullable=False, unique=True)
    email = bd.Column(bd.String(45), nullable=False, unique=True)
    senha = bd.Column(bd.String(25), nullable = False, unique=False)

    def __repr__(self):
        return'<Usuario %r>' % self.nickname
    

class Item(bd.Model):
   idItem = bd.Column(bd.Integer, primary_key=True, autoincrement=True)
   nome = bd.Column(bd.String(25), nullable=False)
   valor = bd.Column(bd.Integer, nullable=False)

   def __repr__(self):
        return'<Item %r>' % self.nome


class Estoque(bd.Model):
    qtd = bd.Column(bd.Integer, nullable=False)
    idUsuario = bd.Column(bd.Integer, bd.ForeignKey('usuario.idUsuario'), primary_key=True)
    idItem = bd.Column(bd.Integer, bd.ForeignKey('item.idItem'), primary_key=True)
    
    def __repr__(self):
        return'<Estoque %r>' % self.qtd

class Mundo(bd.Model):
    idMundo = bd.Column(bd.Integer, primary_key=True, autoincrement=True)
    linguagem = bd.Column(bd.String(8), nullable=False, unique=True)
    modulo = bd.relationship('Modulo')
    def __repr__(self):
        return'<Mundo %r>' % self.linguagem
    
class Modulo(bd.Model):
    idModulo = bd.Column(bd.Integer, primary_key=True, autoincrement=True)
    numero = bd.Column(bd.Integer, nullable=False)
    nome = bd.Column(bd.String(25), nullable=False, unique=True)
    idMundo = bd.Column(bd.Integer, bd.ForeignKey('mundo.idMundo'))
    fase = bd.relationship('Fase', backref='modulo', lazy=True)

    def __repr__(self):
        return'<Modulo %r>' % self.nome

class Fase(bd.Model):
    idFase = bd.Column(bd.Integer, primary_key=True, autoincrement=True)
    materialApoio = bd.Column(bd.String(99), nullable=False)
    exercicio = bd.relationship('Exercicio', backref='fase', lazy=True)
    idModulo = bd.Column(bd.Integer, bd.ForeignKey('modulo.idModulo'))
    def __repr__(self):
        return'<Fase %r>' % self.materialApoio

class Exercicio(bd.Model):
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
    
class Progresso(bd.Model):
    idUsuario = bd.Column(bd.Integer, bd.ForeignKey('usuario.idUsuario'), primary_key=True)
    idFase = bd.Column(bd.Integer, bd.ForeignKey('fase.idFase'), primary_key=True)

    def __repr__(self):
        return'<Progresso %r>' % self.idUsuario
    