from flask import Flask, render_template
from sistema_igreja import app

@app.route('/')
def home():
    return render_template("home.html")
