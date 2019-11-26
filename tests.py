from flask import jsonify

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
            { 'name': 'item 1', 'price': 9.99 }
        ]
    }
]

name = 'Mi Primera Tienda'
i = 0

for dic in stores:
    if dic['name'] == name:
        print( jsonify({ 'items': dic['items'] }) )
        # for item in dic['items']:
        #     print(item['name'])
        #     print(item['price'])
