from models import users

def getAllUsers():
    dataUsers = users.getAllUsers()
    
    return dataUsers

def crearUsuario(nombres):
    users.crearUsuario(nombre=nombres)