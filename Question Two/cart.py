import json
import os

CART_FILE = "cart.json"

def load_cart():
    try:
        if os.path.exists(CART_FILE):
            with open(CART_FILE, "r") as file:
                return json.load(file)
        return []
    except Exception:
        return []

def save_cart(cart_data):
    try:
        with open(CART_FILE, "w") as file:
            json.dump(cart_data, file, indent=2)
    except Exception:
        pass

def add_item(product_id, name, price, quantity):
    cart_data = load_cart()
    
    for item in cart_data:
        if item["product_id"] == product_id:
            item["quantity"] += quantity
            save_cart(cart_data)
            return
    
    cart_data.append({
        "product_id": product_id,
        "name": name,
        "price": price,
        "quantity": quantity
    })
    
    save_cart(cart_data)

def get_cart():
    return load_cart()