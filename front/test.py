import json
import requests

# def exibir_membros(lista_membros):
#     for membro in lista_membros:
#         print(f"{membro['nome']}")

# deletar_livro = requests.delete(url="http://localhost:5000/livros/5")
# atualizar_livro = requests.put(url="http://localhost:5000/livros/4", json='{"titulo": "Harry Potter e a Pedra Filosofal", "autor": "J.K. Rowling"}')

novo_membro = requests.post(url="http://localhost:5000/membros",
                            json="""{"nome": "Gustavo",
                            "data_nascimento": "datetime(2004,6,24)",
                            "numero": "957878236", "endereco": "Rua Anchieta 95",
                            "cargo": "Membro"}""")
# membros = requests.get(url="http://localhost:5000/livros").json()
# exibir_membros(membros)

