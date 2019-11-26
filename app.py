from flask import Flask, jsonify, request, render_template

app = Flask(__name__) # __name__ provee a cada archivo un nombre único

stores= [
    {
        'name': 'Mi Primera Tienda',
        'items': [
            { 'name': 'item 1', 'price': 9.99 },
            { 'name': 'it 2', 'price': 19.99 },
        ]
    },
    {
        'name': 'Segunda Tienda',
        'items': [
            { 'name': 'Un item', 'price': 9.99 },
            { 'name': 'Otro item', 'price': 19.99 },
        ]
    },
]

# @app.route(aquí_va_la_ruta_o_el_endpoint_o_el_request)
'''@app.route('/')
def home():
    return render_template('index.html')'''



# POST /store data: {name:} - obtener info y crear una tienda
# @app.route('/store') # Por default esto es un GET request
@app.route('/store', methods=['POST'])
def createStore():
    request_data = request.get_json()
    if not request_data:
        return 'No se recibió nada'
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)


# GET /store/<string: name> - mandar una tienda
@app.route('/store/<string:name>') # Ej: 127.0.0.1:5000/store/algun_nombre
def getStore(name): # El parámtero tiene que ser igual al <string:paramtero>
    # Iterar para encontrar el deseado
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({ 'data': 'No se encontró la tienda' })


# GET /store - regresar lista de tiendas
@app.route('/stores')
def getStores():
    # return jsonify(stores) # json es un diccionario. Stores NO es un diccionario, es una lista.
    return jsonify({ 'stores': stores }) # agregarle una llave para que sea un diccionario


# POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def createStoreItem(name):
    request_data = request.get_json()
    if not request_data:
        return 'No se recibió nada'

    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)

    return jsonify({ 'data': 'No se encontró la tienda' })


# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def getStoreItem(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({ 'items': store['items'] })
    return jsonify({ 'data': 'No se encontró la tienda' })



app.run(port=5000)
