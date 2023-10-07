from flask import Flask, render_template
from sistema_igreja import app
from sistema_igreja.forms import NovoMembro

@app.route('/')
def home():
    form = NovoMembro()
    return render_template('home.html', form = form)
