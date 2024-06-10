
# main.py
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Define the menu items
menu = [
    {"name": "Coffee", "price": 2.50},
    {"name": "Tea", "price": 1.50},
    {"name": "Pastry", "price": 2.00}
]

# Home page
@app.route('/')
def home():
    return render_template('home.html')

# Menu page
@app.route('/menu')
def menu_page():
    return render_template('menu.html', menu=menu)

# Order page
@app.route('/order')
def order_page():
    return render_template('order.html', menu=menu)

# Submit order
@app.route('/submit-order', methods=['POST'])
def submit_order():
    order = {}
    for item in menu:
        quantity = request.form.get(item["name"])
        if quantity:
            order[item["name"]] = int(quantity)
    return render_template('confirmation.html', order=order)

if __name__ == '__main__':
    app.run(debug=True)
