from main import bd

class Usuario(bd.Model):
    idUsuario = bd.Column(bd.Integer, primary_key=True, auto_increment=True)
    nickname = bd.Column(bd.String(25), nullable=False, unique=True)
    email = bd.Column(bd.String(45), nullable=False, unique=True)
    senha = bd.Column(bd.String(25), nullable = False, unique=False)

    def __repr__(self):
        return'<Usuario %r>' % self.nickname
    

class Item(bd.Model):
   idItem = bd.Column(bd.Integer, primary_key=True, auto_increment=True)
   nome = bd.Column(bd.String(25), nullable=False)
   valor = bd.Column(bd.Integer, nullable=False)

   def __repr__(self):
        return'<Item %r>' % self.nome

 #idMundo INT PRIMARY KEY AUTO_INCREMENT,  
 #linguagem INT NOT NULL,  
 #idModulo INT,  
 #UNIQUE (linguagem)
 #FOREIGN KEY(idModulo) REFERENCES Modulo(idModulo)

class Mundo(bd.Model):
    idMundo = bd.Column(bd.Integer, primary_key=True, auto_increment=True)
    linguagem = bd.Column(bd.String(8), nullable=False, unique=True)
