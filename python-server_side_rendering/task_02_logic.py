#!/usr/bin/python3
"""
Flask application rendering dynamic templates with loops and conditions.
"""
import json
import os
from flask import Flask, render_template

template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'templates'))
app = Flask(__name__, template_folder=template_dir)


@app.route('/items')
def items():
    """Renders items list from items.json."""
    json_path = os.path.join(os.path.dirname(__file__), 'items.json')
    items_list = []

    try:
        with open(json_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            items_list = data.get('items', [])
    except (FileNotFoundError, json.JSONDecodeError):
        items_list = []

    return render_template('items.html', items=items_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
