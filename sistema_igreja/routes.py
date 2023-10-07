from flask import Flask, render_template
from sistema_igreja import app, database
from sistema_igreja.forms import NovoMembro
from sistema_igreja.models import Membro

@app.route('/', methods=["GET", "POST"])
def home():
    form = NovoMembro()
    if form.validate_on_submit():
        membro = Membro(nome= form.nome.data,
                        data_nascimento=form.data_nascimento.data,
                        numero=form.numero.data,
                        endereco = form.endereco.data,
                        cargo=form.cargo.data)
        database.session.add(membro)
        database.session.commit()
        print('rodou')
    return render_template('home.html', form = form)
