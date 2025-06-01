from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

usuarios = []
id_actual = 1

#Ruta para obtener todos los usuarios 
@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    return jsonify(usuarios)

#Ruta para crear un nuevo usuario
@app.route('/usuarios', methods=['POST'])
def crear_usuario():
    global id_actual
    data = request.json
    data['id'] = id_actual
    id_actual += 1
    usuarios.append(data)
    return jsonify(data), 201

#Ruta para actualizar un usuario existente
@app.route('/usuarios/<int:id>', methods=['PUT'])
def actualizar_usuario(id):
    data = request.json
    for u in usuarios:
        if u['id'] == id:
            u.update(data)
            return jsonify(u)
    return {'error': 'Usuario no encontrado'}, 404

#Ruta para eliminar un usuario existente
@app.route('/usuarios/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):
    global usuarios
    usuarios = [u for u in usuarios if u['id'] != id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)