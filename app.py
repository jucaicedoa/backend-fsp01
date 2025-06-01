from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

usuarios = []
id_actual = 1

#Ruta para obtener todos los usuarios 


#Ruta para crear un nuevo usuario


#Ruta para actualizar un usuario existente


#Ruta para eliminar un usuario existente


if __name__ == '__main__':
    app.run(debug=True)