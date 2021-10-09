import mysql.connector

DB = mysql.connector.connect(
    host='localhost',
    user='root',
    password='12345678',
    database='usuarios',
    port=3307
)

def getAllUsers():
    cursor = DB.cursor(dictionary=True)

    cursor.execute('select * from usuarios')

    return cursor.fetchall()

def crearUsuario(nombre, apellidos, email):
    return true