from flask import Flask
from app.database import init_app
from flask_cors import CORS
from app.views import *


app = Flask(__name__)

init_app(app)

CORS(app, resources={r"/api/*": {"origins": "*"}})


# # app.route('/', methods=['GET'])(index)
# app.route('/api/productos', methods=['GET'])(get_productos)
# # app.route('/api/productos/<id>', methods=['GET'])(get_productos)
# app.route('/api/productos/', methods=['POST'])(create_productos)

app.add_url_rule('/', 'index', index)
app.add_url_rule('/api/saludar', 'saludar', saludar)
app.add_url_rule('/api/productos', 'get_productos', get_productos, methods=['GET'])
app.add_url_rule('/api/productos/<int:id>', 'get_producto', get_producto, methods=['GET'])
app.add_url_rule('/api/productos/', 'create_productos', create_productos, methods=['POST'])
app.add_url_rule('/api/productos/<int:id>', 'update_productos', update_productos, methods=['PUT'])
app.add_url_rule('/api/productos/<int:id>', 'delete_productos', delete_productos, methods=['DELETE'])


if __name__ == '__main__':
    app.run(debug=True)