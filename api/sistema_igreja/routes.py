from flask import Flask, render_template, request, jsonify
from sistema_igreja import app, database
from sistema_igreja.models import Membro
import datetime
import json

@app.route('/membros', methods=["POST"])
def novo_membro():
    membro_novo = request.get_json()
    membro_novo = json.loads(membro_novo)
    #date = datetime.date(int(membro_novo['data_nascimento'][:4]), int(membro_novo['data_nascimento'][5:7]), int(membro_novo['data_nascimento'][8:]))
    membro = Membro(nome=membro_novo['nome'],
                    data_nascimento=membro_novo['data_nascimento'], #membro_novo['data_nascimento']
                    numero=membro_novo['numero'],
                    endereco=membro_novo['endereco'],
                    cargo=membro_novo['cargo'])
    database.session.add(membro)
    database.session.commit()
    membro_json = Membro.query.filter_by(nome=membro_novo['nome']).first().__dict__
    treat = membro_json.pop('_sa_instance_state')
    return jsonify(membro_json)

@app.route('/membros', methods=["GET"])
def mostrar_membros():
    lista_membros = []
    membros = Membro.query.all()
    for l in membros:
        l = l.__dict__
        treat = l.pop('_sa_instance_state')
        lista_membros.append(l)
    return jsonify(lista_membros)
