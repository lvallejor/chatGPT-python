from flask import Flask, jsonify, request

app = Flask(__name__)

from products import products

# Testing Route
@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'response': 'pong!'})

# Get Data Routes
@app.route('/products')
def getProducts():
    # return jsonify(products)
    return jsonify({'products': products})


@app.route('/products/<string:product_name>')
def getProduct(product_name):
    productsFound = [
        product for product in products if product['name'] == product_name.lower()]
    if (len(productsFound) > 0):
        return jsonify({'product': productsFound[0]})
    return jsonify({'message': 'Product Not found'})

# Create Data Routes
@app.route('/products', methods=['POST'])
def addProduct():
    new_product = {
        'name': request.json['name'],
        'price': request.json['price'],
        'quantity': 10
    }
    products.append(new_product)
    return jsonify({'products': products})

if __name__ == '__main__':
    app.run(debug=True, port=4000)