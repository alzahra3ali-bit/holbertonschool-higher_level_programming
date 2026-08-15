#!/usr/bin/python3
"""
Flask application displaying product data from JSON, CSV, or SQLite database.
"""
import csv
import json
import os
import sqlite3
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


def read_sql_db(filepath):
    """Reads products from a SQLite database."""
    products = []
    conn = sqlite3.connect(filepath)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, category, price FROM Products")
    rows = cursor.fetchall()

    for row in rows:
        products.append({
            'id': row[0],
            'name': row[1],
            'category': row[2],
            'price': float(row[3])
        })

    conn.close()
    return products


@app.route('/products')
def display_products():
    """Displays products based on source (json, csv, sql) and optional id query parameters."""
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error="Wrong source")

    db_path = os.path.join(os.path.dirname(__file__), 'products.db')
    json_path = os.path.join(os.path.dirname(__file__), 'products.json')
    csv_path = os.path.join(os.path.dirname(__file__), 'products.csv')

    products = []
    try:
        if source == 'sql':
            products = read_sql_db(db_path)
        elif source == 'json':
            products = read_json_file(json_path)
        elif source == 'csv':
            products = read_csv_file(csv_path)
    except sqlite3.Error:
        return render_template('product_display.html', error="Database error")
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
