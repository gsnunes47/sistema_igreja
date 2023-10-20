from flask import Flask, render_template, jsonify, redirect, url_for
from forms import NovoMembro, EditarMembro
import datetime
import requests

app = Flask('__main__') #, template_folder=r'sistema_igreja\templates')
app.config['SECRET_KEY'] = 'chavesecreta'

@app.route('/', methods=['GET', 'POST'])
def home():
    form = NovoMembro()
    lista_membros = requests.get('http://127.0.0.1:5000/membros').json()
    mes_atual = datetime.datetime.now().month
    if form.is_submitted():
        data = form.data_nascimento.data.strftime('%d-%m-%Y - %H:%M:%S')[:10]
        membro = f"""{"{"}"nome": "{form.nome.data}", "data_nascimento": "{data}", "numero": "{form.numero.data}", "endereco": "{form.endereco.data}", "cargo": "{form.cargo.data}"{"}"}"""
        membro = jsonify(membro)
        membro = membro.json
        novo_membro = requests.post(url='http://localhost:5000/membros', json=membro)
        return redirect(url_for('home'))
    return render_template('home.html', form=form, lista_membros=lista_membros, mes_atual=str(mes_atual))  

@app.route('/excluir/<id>')
def excluir(id):
    id = int(id)
    lista_membros = requests.get('http://127.0.0.1:5000/membros').json()
    membro_excluido = ''
    for membro in lista_membros:
        if membro['id'] == id:
            membro_excluido = membro
    excluir_membro = requests.delete(url='http://localhost:5000/membros', json=membro_excluido)
    return redirect(url_for('home'))

@app.route('/editar/<id>', methods=['POST', 'GET'])
def editar(id):
    id = int(id)
    form = EditarMembro()
    if form.is_submitted():
        data = form.data_nascimento.data.strftime('%d-%m-%Y - %H:%M:%S')[:10]
        edicao = f"""{"{"}"id": "{id}", "nome": "{form.nome.data}", "data_nascimento": "{data}", "numero": "{form.numero.data}", "endereco": "{form.endereco.data}", "cargo": "{form.cargo.data}"{"}"}"""
        edicao = jsonify(edicao)
        edicao = edicao.json
        editar_membro = requests.put(url='http://localhost:5000/membros', json=edicao)
        return redirect(url_for('home'))
    return render_template('editar.html', form=form)

if __name__ == '__main__':
    app.run(debug=True, port=8081)
