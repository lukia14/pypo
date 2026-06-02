from app import bd
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


    

    