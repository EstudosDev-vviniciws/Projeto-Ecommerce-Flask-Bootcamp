from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

class CadastroForm(FlaskForm):
    usuario = StringField(label='Username:')
    email = StringField(label='E-mail:')
    senha1 = PasswordField(label='Senha:')
    senha2 = PasswordField(label='Confirmação de Senha:')
    submit = SubmitField(label='Cadastrar')
    