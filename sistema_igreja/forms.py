from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, SelectField
from wtforms.validators import DataRequired, Length

class NovoMembro(FlaskForm):
    nome = StringField("Nome", validators=[DataRequired()])
    data_nascimento = DateField("Data de nascimento", validators=[DataRequired()])
    numero = StringField("Número", validators=[DataRequired(), Length(9, 11)])
    endereco = StringField("Endereço", validators=[DataRequired()])
    botao_confirmacao = SubmitField("Cadastrar")
    cargo = SelectField("Cargo Eclesiastico", choices = [('pastor', 'Pastor'), ('diacono', 'Diacono'), ('presbítero', 'Presbítero'), ('cooperador', 'Coorperador'), ('membro', 'Membro')])