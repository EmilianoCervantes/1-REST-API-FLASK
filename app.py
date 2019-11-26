from flask import Flask, jsonify, request

app = Flask(__name__) # __name__ provee a cada archivo un nombre único

stores= [
    {
        'name': 'Mi Primera Tienda',
        'item': [
            { 'name': 'item 1', 'price': 9.99 }
        ]
    }
]

# @app.route(aquí_va_la_ruta_o_el_endpoint_o_el_request)
'''@app.route('/')
def home():
    return "Hola mundo"'''

# POST /store data: {name:} - crear una tienda
# @app.route('/store') # Por default esto es un GET request
@app.route('/store', methods=['POST'])
def createStore():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify({ 'Nueva tienda': stores })

# GET /store/<string: name> - mandar una tienda
@app.route('/store/<string:name>')
def getStore(name): # El parámtero tiene que ser igual al <string:paramtero>
    # Iterar para encontrar el deseado
    for dic in stores:
        for val in dic.values():
            if val['name'] == name:
                return jsonify({ 'Buscado: ': val })
    return jsonify({ 'Buscado: ': 'No se encontró el elemento' })

# GET /store - regresar lista de tiendas
@app.route('/stores')
def getStores():
    # return jsonify(stores) # json es un diccionario. Stores NO es un diccionario, es una lista.
    return jsonify({ 'stores': stores }) # agregarle una llave para que sea un diccionario

# POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def createStoreItem(name, price):
    # Iterar las tiendas
    tienda = {}
    pass

# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def getStoreItem(name):
    for dic in stores:
        for val in dic.values():
            

app.run(port=5000)
