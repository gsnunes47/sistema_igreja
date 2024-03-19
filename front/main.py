from flask import Flask, render_template, jsonify, redirect, url_for
from forms import NovoMembro, EditarMembro, FiltarMembros
import datetime
import requests

app = Flask('__main__', static_folder="static") #, template_folder=r'sistema_igreja\templates')
app.config['SECRET_KEY'] = 'chavesecreta'

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/membros', methods=['GET', 'POST'])
def membros():
    form = NovoMembro()
    form2 = FiltarMembros()
    form3 = EditarMembro()
    lista_membros = requests.get('https://api-igreja.onrender.com/membros').json()
    mes_atual = datetime.datetime.now().month
    if mes_atual <  10:
        mes_atual = '0' + str(mes_atual)
    lista_aniversariantes = []
    for membro in lista_membros:
        if membro['data_nascimento'][3:5] == mes_atual:
            lista_aniversariantes.append(membro)
    return render_template('membros.html', form=form, form2=form2, form3=form3, lista_membros=lista_membros, lista_aniversariantes=lista_aniversariantes, mes_atual=str(mes_atual))  

@app.route('/novo_membro', methods=['GET', 'POST'])
def novo_membro():
    form = NovoMembro()
    form2 = FiltarMembros()
    lista_membros = requests.get('https://api-igreja.onrender.com/membros').json()
    mes_atual = datetime.datetime.now().month
    lista_aniversariantes = []
    for membro in lista_membros:
        if membro['data_nascimento'][3:5] == str(mes_atual):
            lista_aniversariantes.append(membro)
    if form.is_submitted():
        data = form.data_nascimento.data.strftime('%d-%m-%Y - %H:%M:%S')[:10]
        membro = f"""{"{"}"nome": "{form.nome.data}", "data_nascimento": "{data}", "numero": "{form.numero.data}", "endereco": "{form.endereco.data}", "cargo": "{form.cargo.data}"{"}"}"""
        membro = jsonify(membro)
        membro = membro.json
        novo_membro = requests.post(url='https://api-igreja.onrender.com/membros', json=membro)
        return redirect(url_for('membros'))
    return render_template('membros.html', form=form, form2=form2, lista_membros=lista_membros, lista_aniversariantes=lista_aniversariantes,  mes_atual=str(mes_atual))  

@app.route('/filtrar_membros', methods=['GET', 'POST'])
def filtrar_membros():
    form = NovoMembro()
    form2 = FiltarMembros()
    form3 = EditarMembro()
    lista_membros = requests.get('https://api-igreja.onrender.com/membros').json()
    mes_atual = datetime.datetime.now().month
    lista_aniversariantes = []
    for membro in lista_membros:
        if membro['data_nascimento'][3:5] == str(mes_atual):
            lista_aniversariantes.append(membro)
    if form2.is_submitted():
        # data = form2.data_nascimento.data.strftime('%d-%m-%Y - %H:%M:%S')[:10]
        lista_membros = requests.get('https://api-igreja.onrender.com/membros').json()
        membro_filtrado = []
        for membro in lista_membros:
            if form2.cargo.data == 'vazio':
                if form2.nome.data in membro['nome']:
                    membro_filtrado.append(membro)
            else:
                if form2.nome.data in membro['nome'] and membro['cargo'] == form2.cargo.data:
                    membro_filtrado.append(membro)
        return render_template('membros.html', form=form, form2=form2, form3=form3, lista_membros=membro_filtrado, lista_aniversariantes=lista_aniversariantes, mes_atual=str(mes_atual))  
    return render_template('membros.html', form=form, form2=form2, form3=form3, lista_membros=lista_membros, lista_aniversariantes=lista_aniversariantes, mes_atual=str(mes_atual))  

@app.route('/excluir/<id>')
def excluir(id):
    id = int(id)
    lista_membros = requests.get('https://api-igreja.onrender.com/membros').json()
    membro_excluido = ''
    for membro in lista_membros:
        if membro['id'] == id:
            membro_excluido = membro
    excluir_membro = requests.delete(url='https://api-igreja.onrender.com/membros', json=membro_excluido)
    return redirect(url_for('membros'))

@app.route('/editar/<id>', methods=['POST', 'GET'])
def editar(id):
    form = EditarMembro()
    id = int(id)
    membros = requests.get('https://api-igreja.onrender.com/membros').json()
    if form.is_submitted():
        data = form.data_nascimento.data.strftime('%d-%m-%Y - %H:%M:%S')[:10]
        edicao = f"""{"{"}"id": "{id}", "nome": "{form.nome.data}", "data_nascimento": "{data}", "numero": "{form.numero.data}", "endereco": "{form.endereco.data}", "cargo": "{form.cargo.data}"{"}"}"""
        edicao = jsonify(edicao)
        edicao = edicao.json
        editar_membro = requests.put(url='https://api-igreja.onrender.com/membros', json=edicao)
        return redirect(url_for('membros'))
    return render_template('editar.html', form3=form)

if __name__ == '__main__':
    app.run(debug=True, port=8081)
