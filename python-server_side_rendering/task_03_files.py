from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json_file(filepath):
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return []

def read_csv_file(filepath):
    try:
        with open(filepath, newline='') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
            return data
    except FileNotFoundError:
        return []

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source == 'json':
        products = read_json_file('products.json')
    elif source == 'csv':
        products = read_csv_file('products.csv')
    else:
        return render_template('product_display.html', error="Wrong source parameter. Use 'json' or 'csv'.")

    if product_id:
        products = [product for product in products if str(product['id']) == str(product_id)]
        if not products:
            return render_template('product_display.html', error="Product not found.")

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

