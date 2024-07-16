from flask import Flask, render_template, request
import json
import csv
import sqlite3

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

def read_sqlite_db():
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Products")
        rows = cursor.fetchall()
        conn.close()
        # Convert rows to dictionary format
        products = [{"id": row[0], "name": row[1], "category": row[2], "price": row[3]} for row in rows]
        return products
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source == 'json':
        products = read_json_file('products.json')
    elif source == 'csv':
        products = read_csv_file('products.csv')
    elif source == 'sql':
        products = read_sqlite_db()
    else:
        return render_template('product_display.html', error="Wrong source parameter. Use 'json', 'csv', or 'sql'.")

    if product_id:
        products = [product for product in products if str(product['id']) == str(product_id)]
        if not products:
            return render_template('product_display.html', error="Product not found.")

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

