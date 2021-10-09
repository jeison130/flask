from flask import Flask, render_template, request
from controllers import users

app = Flask(__name__)

@app.get('/')
def home():
    dataUsers = users.getAllUsers()
    
    return render_template('index.html', users = dataUsers)

@app.get('/crear')
def crearUsuario():
    return render_template('crearUsuario.html')

@app.post('/guardar')
def guardarUsuario():
    data = request.form

    print(data)
    return 'Guardando'

app.run(debug=True)