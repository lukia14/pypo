from app import bd
class UsuarioModel(bd.Model):
    __tablename__ = 'Usuario'

    idUsuario = bd.Column(bd.Integer, primary_key=True, autoincrement=True)
    nickname = bd.Column(bd.String(25), nullable=False, unique=True)
    email = bd.Column(bd.String(45), nullable=False, unique=True)
    senha = bd.Column(bd.String(25), nullable = False, unique=False)

    def modeloUsuario(self,form):
        nickname = form.get('nickname')
        email = form.get('email')
        senha = form.get('senha')
        email = form.get('email')
        usuario = UsuarioModel(nickname=nickname, email=email, senha=senha)
        return usuario