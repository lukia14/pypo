from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators, IntegerField
from wtforms.validators import DataRequired, Length

class FormularioUsuario(FlaskForm):
    nickname = StringField("Nickname", validators=[DataRequired(), Length(min=1, max=20)])
    email = StringField('Email', validators=[DataRequired(), Length(min=1, max=35)])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(min=1, max=35)])
    enviar = SubmitField('Enviar')
class FormularioAlterarSenha(FlaskForm):
    senhaAntiga = PasswordField('Senha Antiga', validators=[DataRequired(), Length(min=1, max=35)])
    novaSenha = PasswordField('Nova Senha', validators=[DataRequired(), Length(min=1, max=35)])
    confirmarSenha = PasswordField('Confirmar Nova Senha', validators=[DataRequired(), Length(min=1, max=35), validators.EqualTo('novaSenha', message='As senhas devem coincidir')])
    enviar = SubmitField('Alterar Senha')

class FormularioExercicio(FlaskForm):
    idExercicio = IntegerField("Id do Exercício", validators=[DataRequired()],render_kw={'readonly': True})
    numero = IntegerField("Número do Exercício", validators=[DataRequired()])
    idFase = IntegerField("Id da Fase", validators=[DataRequired()])
    titulo = StringField("Título", validators=[DataRequired(), Length(min=1, max=35)])
    enunciado = StringField("Enunciado", validators=[DataRequired(), Length(min=1, max=99)])
    alternativaA = StringField("Alternativa A", validators=[DataRequired(), Length(min=1, max=99)])
    alternativaB = StringField("Alternatica B", validators=[DataRequired(), Length(min = 1, max=99)])
    alternativaC = StringField("Alternativa C", validators=[DataRequired(),Length(min=1, max=99)])
    alternativaD = StringField("ALternativa D", validators=[DataRequired(), Length(min=1, max=99)])
    resposta = StringField("Alternativa da Resposta",validators=[DataRequired(),Length(min=1, max=1)])
    
    enviar = SubmitField("Criar Exercício")

#     class Item(bd.Model):
#    idItem = bd.Column(bd.Integer, primary_key=True, autoincrement=True)
#    nome = bd.Column(bd.String(25), nullable=False)
#    valor = bd.Column(bd.Integer, nullable=False)

class FormularioItem(FlaskForm):
    idItem = IntegerField("Id do Item", validators= [DataRequired()])
    nome = StringField("Nome do Item", validators=[DataRequired(), Length(min=1, max = 30)])
    valor = IntegerField("Valor do Item", validators=[DataRequired(), Length(min=1, max = 5)])

    enviar = SubmitField("Criar Item")

