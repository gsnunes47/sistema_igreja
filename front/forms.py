from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, SelectField, PasswordField
from wtforms.validators import DataRequired, Length

class NovoMembro(FlaskForm):
    nome = StringField("Nome", validators=[DataRequired()])
    data_nascimento = DateField("Data de nascimento", validators=[DataRequired()])
    numero = StringField("Número de telefone", validators=[DataRequired(), Length(9, 11)])
    endereco = StringField("Endereço", validators=[DataRequired()])
    cargo = SelectField("Cargo Eclesiastico", choices = [('pastor', 'Pastor'), ('diacono', 'Diacono'), ('presbítero', 'Presbítero'), ('cooperador', 'Cooperador'), ('membro', 'Membro')])
    botao_confirmacao = SubmitField("Cadastrar")
    
class EditarMembro(FlaskForm):
    nome = StringField("Nome", validators=[DataRequired()])
    data_nascimento = DateField("Data de nascimento", validators=[DataRequired()])
    numero = StringField("Número", validators=[DataRequired(), Length(9, 11)])
    endereco = StringField("Endereço", validators=[DataRequired()])
    cargo = SelectField("Cargo Eclesiastico", choices = [('pastor', 'Pastor'), ('diacono', 'Diacono'), ('presbítero', 'Presbítero'), ('cooperador', 'Cooperador'), ('membro', 'Membro')])
    botao_confirmacao = SubmitField("Editar")

class FiltarMembros(FlaskForm):
    nome = StringField("Nome")
    cargo = SelectField("Cargo Eclesiastico", choices = [('vazio', 'Selecione um cargo'), ('pastor', 'Pastor'), ('diacono', 'Diacono'), ('presbítero', 'Presbítero'), ('cooperador', 'Cooperador'), ('membro', 'Membro')])
    botao_confirmacao = SubmitField("Filtrar")

class TestLogin(FlaskForm):
    login = StringField("Login")
    senha = PasswordField("Senha")
    botao_confirmacao = SubmitField("Login")
