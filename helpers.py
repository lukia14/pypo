from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators
from wtforms.validators import DataRequired, Length

class FormularioUsuario(FlaskForm):
    nickname = StringField("Nickname", validators=[DataRequired(), Length(min=1, max=20)])
    email = StringField('Email', validators=[DataRequired(), Length(min=1, max=35)])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(min=1, max=35)])
    enviar = SubmitField('Enviar')