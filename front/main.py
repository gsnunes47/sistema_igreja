from flask import Flask, render_template, jsonify, redirect, url_for, session
from flask_jwt_extended import JWTManager, create_access_token, get_jwt_identity, jwt_required
from flask_login import LoginManager
from forms import NovoMembro, EditarMembro, FiltarMembros, TestLogin
from werkzeug.security import check_password_hash
import datetime
import requests
import pyperclip

app = Flask('__main__', static_folder="static") #, template_folder=r'sistema_igreja\templates')
app.config['SECRET_KEY'] = 'chavesecreta'

jwt = JWTManager(app)
app.config["JWT_SECRET_KEY"] = "chavesecretajwt"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = datetime.timedelta(hours=0.25)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = datetime.timedelta(days=1)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/membros', methods=['GET', 'POST'])
@jwt_required()
def membros():
    form = NovoMembro()
    form2 = FiltarMembros()
    form3 = EditarMembro()
    lista_membros = requests.get('http://127.0.0.1:5000/membros').json()
    mes_atual = datetime.datetime.now().month
    if mes_atual <  10:
        mes_atual = '0' + str(mes_atual)
    lista_aniversariantes = []
    for membro in lista_membros:
        if membro['data_nascimento'][3:5] == mes_atual:
            lista_aniversariantes.append(membro)
    return render_template('membros.html', form=form, form2=form2, form3=form3, lista_membros=lista_membros, lista_aniversariantes=lista_aniversariantes, mes_atual=str(mes_atual))  

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = TestLogin()
    if form.is_submitted():
        req = requests.post('http://127.0.0.1:5000/login', json={"email": form.login.data, "senha": form.senha.data})
        if req.json()['auth'] == True:
            token = 'Bearer '+ str(create_access_token(identity=form.login.data))
            return redirect(url_for('membros', headers={'authorization': token}))
    return render_template('test.html', form=form)

@app.route('/novo_membro', methods=['GET', 'POST'])
@jwt_required()
def novo_membro():
    form = NovoMembro()
    form2 = FiltarMembros()
    lista_membros = requests.get('http://127.0.0.1:5000/membros').json()
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
        novo_membro = requests.post(url='http://127.0.0.1:5000/membros', json=membro)
        return redirect(url_for('membros'))
    return render_template('membros.html', form=form, form2=form2, lista_membros=lista_membros, lista_aniversariantes=lista_aniversariantes,  mes_atual=str(mes_atual))  

@app.route('/filtrar_membros', methods=['GET', 'POST'])
@jwt_required()
def filtrar_membros():
    form = NovoMembro()
    form2 = FiltarMembros()
    form3 = EditarMembro()
    lista_membros = requests.get('http://127.0.0.1:5000/membros').json()
    mes_atual = datetime.datetime.now().month
    lista_aniversariantes = []
    for membro in lista_membros:
        if membro['data_nascimento'][3:5] == str(mes_atual):
            lista_aniversariantes.append(membro)
    if form2.is_submitted():
        # data = form2.data_nascimento.data.strftime('%d-%m-%Y - %H:%M:%S')[:10]
        lista_membros = requests.get('http://127.0.0.1:5000/membros').json()
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
@jwt_required()
def excluir(id):
    id = int(id)
    lista_membros = requests.get('http://127.0.0.1:5000/membros').json()
    membro_excluido = ''
    for membro in lista_membros:
        if membro['id'] == id:
            membro_excluido = membro
    excluir_membro = requests.delete(url='http://127.0.0.1:5000/membros', json=membro_excluido)
    return redirect(url_for('membros'))

@app.route('/editar/<id>', methods=['POST', 'GET'])
@jwt_required()
def editar(id):
    form = EditarMembro()
    id = int(id)
    membros = requests.get('http://127.0.0.1:5000/membros').json()
    if form.is_submitted():
        data = form.data_nascimento.data.strftime('%d-%m-%Y - %H:%M:%S')[:10]
        edicao = f"""{"{"}"id": "{id}", "nome": "{form.nome.data}", "data_nascimento": "{data}", "numero": "{form.numero.data}", "endereco": "{form.endereco.data}", "cargo": "{form.cargo.data}"{"}"}"""
        edicao = jsonify(edicao)
        edicao = edicao.json
        editar_membro = requests.put(url='http://127.0.0.1:5000/membros', json=edicao)
        return redirect(url_for('membros'))
    return render_template('editar.html', form3=form)

if __name__ == '__main__':
    app.run(debug=True, port=8081)
