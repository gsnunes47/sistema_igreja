from sistema_igreja import database, app
from sistema_igreja.models import Membro

with app.app_context():
    database.create_all()
