from flask import Flask, render_template, jsonify
from forms import NovoMembro
import datetime
import requests

app = Flask('__main__') #, template_folder=r'sistema_igreja\templates')
app.config['SECRET_KEY'] = 'chavesecreta'

@app.route('/', methods=['GET', 'POST'])
def home():
    form = NovoMembro()
    if form.validate_on_submit:
        banana = f"""{"{"}"nome": "{form.nome.data}", "data_nascimento": "{form.data_nascimento.data}", "numero": "{form.numero.data}", "endereco": "{form.endereco.data}", "cargo": "{form.cargo.data}"{"}"}"""
        banana = jsonify(banana)
        banana = banana.json
        novo_membro = requests.post(url='http://localhost:5000/membros', json=banana)
    return render_template('home.html', form=form)  

if __name__ == '__main__':
    app.run(debug=True, port=8081)
