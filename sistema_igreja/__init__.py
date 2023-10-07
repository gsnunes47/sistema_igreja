from flask import Flask

app = Flask('__main__')

from sistema_igreja import routes
