from main import bd

class Usuario(bd.Model):
    idUsuario = bd.Column(bd.Integer, primary_key=True, auto_increment=True)
    nickname = bd.Column(bd.String(25), nullable=False, unique=True)
    email = bd.Column(bd.String(45), nullable=False, unique=True)
    senha = bd.Column(bd.String(25), nullable = False, unique=False)

    def __repr__(self):
        return'<Usuario %r>' % self.nickname