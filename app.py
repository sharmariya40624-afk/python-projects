from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import json
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # For session handling

# Load menu data
with open('data/menu.json') as f:
    menu_items = json.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/menu')
def menu():
    return render_template('menu.html', menu_items=menu_items)

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    item_id = int(request.form['item_id'])
    item = next((item for item in menu_items if item['id'] == item_id), None)
    if not item:
        return 'Item not found', 404

    cart = session.get('cart', [])
    cart.append(item)
    session['cart'] = cart
    return redirect(url_for('menu'))

@app.route('/cart')
def cart():
    cart = session.get('cart', [])
    total = sum(item['price'] for item in cart)
    return render_template('cart.html', cart=cart, total=total)

@app.route('/checkout', methods=['POST'])
def checkout():
    session.pop('cart', None)  # Clear cart
    return render_template('order_success.html')

if __name__ == '__main__':
    app.run(debug=True)
