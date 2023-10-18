from flask import Flask, render_template, jsonify, redirect, url_for
from forms import NovoMembro
import datetime
import requests

app = Flask('__main__') #, template_folder=r'sistema_igreja\templates')
app.config['SECRET_KEY'] = 'chavesecreta'

@app.route('/', methods=['GET', 'POST'])
def home():
    form = NovoMembro()
    lista_membros = requests.get('http://127.0.0.1:5000/membros').json()
    mes_atual = datetime.datetime.now().month
    if form.validate_on_submit():
        data = form.data_nascimento.data.strftime('%d-%m-%Y - %H:%M:%S')[:10]
        membro = f"""{"{"}"nome": "{form.nome.data}", "data_nascimento": "{data}", "numero": "{form.numero.data}", "endereco": "{form.endereco.data}", "cargo": "{form.cargo.data}"{"}"}"""
        membro = jsonify(membro)
        membro = membro.json
        novo_membro = requests.post(url='http://localhost:5000/membros', json=membro)
        return redirect(url_for('home'))
    return render_template('home.html', form=form, lista_membros=lista_membros)  

if __name__ == '__main__':
    app.run(debug=True, port=8081)
