import requests
import datetime

def filtrar(nome = None, cargo = None, data_nascimento = None, endereco = None, id = None, numero = None):
    filtros = []
    if nome:
        filtros.append(nome)
    if cargo:
        filtros.append(cargo)
    if data_nascimento:
        filtros.append(data_nascimento)
    if endereco:
        filtros.append(endereco)
    if id:
        filtros.append(id)
    if numero:
        filtros.append(numero)
    return filtros

filtrar

# lista_membros = requests.get('https://api-igreja.onrender.com/membros').json()
# lista_filtrada = []
# data_filter = '23-11-2000'
# cargo_filter = 'pastor'
# nome_filter = 'pedro'
# numero = '11987653456'
# for membro in lista_membros:
    
#     # if membro["cargo"]: #form2.data_nascimento.cargo 
#     #     if membro["cargo"] == cargo_filter:
#     #         lista_filtrada.append(membro)
# print(lista_filtrada)
