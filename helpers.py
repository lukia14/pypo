from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators, IntegerField
from wtforms.validators import DataRequired, Length

class FormularioUsuario(FlaskForm):
    nickname = StringField("Nickname", validators=[DataRequired(), Length(min=1, max=20)])
    email = StringField('Email', validators=[DataRequired(), Length(min=1, max=35)])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(min=1, max=35)])
    enviar = SubmitField('Enviar')

class FormularioExercicio(FlaskForm):
    idExercicio = StringField("Id do Exercício",validators=[DataRequired(), Length(min=1,max=11)])
    numero = IntegerField("Número do Exercício", validators=[DataRequired(), Length(min=1, max=11)])
    titulo = StringField("Título", validators=[DataRequired(), Length(min=1, max=35)])
    enunciado = StringField("Enunciado", validators=[DataRequired(), Length(min=1, max=99)])
    alternativaA = StringField("Alternativa A", validators=[DataRequired(), Length(min=1, max=99)])
    alternativaB = StringField("Alternatica B", validators=[DataRequired(), Length(min = 1, max=99)])
    alternativaC = StringField("Alternativa C", validators=[DataRequired(),Length(min=1, max=99)])
    alternativaD = StringField("ALternativa D", validators=[DataRequired(), Length(min=1, max=99)])
    resposta = StringField("Alternativa da Resposta",validators=[DataRequired(),Length(min=1, max=1)])
    
    enviar = SubmitField("Criar Exercício")



