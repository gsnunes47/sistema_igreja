from sistema_igreja import database

class Membro(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    nome = database.Column(database.String, nullable=False)
    data_nascimento = database.Column(database.DateTime, nullable=False)
    numero = database.Column(database.String, nullable=False)
    endereço = database.Column(database.String, nullable=False)
