from flask import jsonify, request, make_response
from app.models import Producto

def index():
    response = {'message': 'Hello, World!'}
    return jsonify(response)

def saludar():
    response = {'message': 'saludos'}
    return jsonify(response)

def get_productos():
    productos = Producto.get_all()
    lista_productos = [producto.serealize() for producto in productos]
    return jsonify(lista_productos)

def get_producto(id):
    producto = Producto.get(id)
    if not producto:
        return jsonify({'message': 'No se encontro el producto'}), 404
    return jsonify(producto.serealize())

def create_productos():
    if request.method == 'OPTIONS':
        return _build_cors_preflight_response()
    
    data = request.get_json()
    nuevo_producto = Producto(
        None,
        data['categoria'],
        data['nombre_producto'],
        data['material'],
        data['descripcion'],
        data['precio'],
        data['imagen']
    )
    nuevo_producto.save()
    response = jsonify({'message': 'Producto creado'})
    return _corsify_actual_response(response), 201

def update_productos(id):
    if request.method == 'OPTIONS':
        return _build_cors_preflight_response()
    
    data = request.get_json()
    editado = Producto.get(id)
    if not editado:
        response = jsonify({'message': 'No se encontró el producto'})
        return _corsify_actual_response(response), 404
    editado.categoria = data['categoria']
    editado.nombre_producto = data['nombre_producto']
    editado.material = data['material']
    editado.descripcion = data['descripcion']
    editado.precio = data['precio']
    editado.imagen = data['imagen']
    editado.save()
    response = jsonify({'message': 'Producto editado'})
    return _corsify_actual_response(response), 200

def delete_productos(id):
    if request.method == 'OPTIONS':
        return _build_cors_preflight_response()
    
    editado = Producto.get(id)
    if not editado:
        response = jsonify({'message': 'No se encontró el producto'})
        return _corsify_actual_response(response), 404
    editado.delete()
    response = jsonify({'message': 'Producto eliminado'})
    return _corsify_actual_response(response), 200

def get_productos_by_categoria(categoria):
    productos = Producto.get_productos_by_categoria(categoria)
    lista_productos = [producto.serealize() for producto in productos]
    return jsonify(lista_productos)

def categorias():
    categorias = Producto.get_categorias()
    return jsonify(categorias)

def _build_cors_preflight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "Content-Type")
    response.headers.add('Access-Control-Allow-Methods', "GET, POST, PUT, DELETE, OPTIONS")
    return response
def _corsify_actual_response(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response