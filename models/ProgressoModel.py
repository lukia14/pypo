from app import bd
class ProgressoModel(bd.Model):
    __tablename__ = 'Progresso'
    idUsuario = bd.Column(bd.Integer, bd.ForeignKey('usuario.idUsuario'), primary_key=True)
    idFase = bd.Column(bd.Integer, bd.ForeignKey('fase.idFase'), primary_key=True)

    def __repr__(self):
        return'<Progresso %r>' % self.idUsuario