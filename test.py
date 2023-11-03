import requests

id = 4

membros = requests.get('https://api-igreja.onrender.com/membros').json()
for membro in membros:
    if membro['id'] == id:
        dados_membro = membro
print(dados_membro)
