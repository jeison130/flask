from flask import Flask, render_template
from controllers import users

app = Flask(__name__)

@app.get('/')
def home():
    dataUsers = users.getAllUsers()
    
    return render_template('index.html', users = dataUsers)

app.run(debug=True)