#!/usr/bin/python3
"""
Flask application displaying product data from JSON or CSV files with filtering.
"""
import csv
import json
import os
from flask import Flask, render_template, request

template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'templates'))
app = Flask(__name__, template_folder=template_dir)


def read_json_file(filepath):
    """Reads products from a JSON file."""
    with open(filepath, 'r', encoding='utf-8') as file:
        return json.load(file)


def read_csv_file(filepath):
    """Reads products from a CSV file."""
    products = []
    with open(filepath, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            products.append({
                'id': int(row['id']),
                'name': row['name'],
                'category': row['category'],
                'price': float(row['price'])
            })
    return products


@app.route('/products')
def display_products():
    """Displays products based on source and optional id query parameters."""
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source")

    filename = 'products.json' if source == 'json' else 'products.csv'
    filepath = os.path.join(os.path.dirname(__file__), filename)

    try:
        if source == 'json':
            products = read_json_file(filepath)
        else:
            products = read_csv_file(filepath)
    except Exception:
        products = []

    if product_id:
        try:
            target_id = int(product_id)
            products = [p for p in products if p['id'] == target_id]
        except ValueError:
            products = []

        if not products:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=products)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
