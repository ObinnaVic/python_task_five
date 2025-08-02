from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import cart
import math

app = FastAPI()

class Product(BaseModel):
    id: int
    name: str
    price: float

products_db = [
    Product(id=1, name="Laptop", price=999.99),
    Product(id=2, name="Mouse", price=25.50),
    Product(id=3, name="Keyboard", price=75.00),
    Product(id=4, name="Monitor", price=299.99),
    Product(id=5, name="Headphones", price=149.99)
]

@app.get("/products/")
def get_products():
    return products_db

@app.post("/cart/add")
def add_to_cart(product_id: int, qty: int):
    product = None
    for p in products_db:
        if p.id == product_id:
            product = p
            break
    
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    cart.add_item(product_id, product.name, product.price, qty)
    return {"message": f"Added {qty} x {product.name} to cart"}

@app.get("/cart/checkout")
def checkout():
    cart_items = cart.get_cart()
    total = 0
    
    for item in cart_items:
        item_total = item["price"] * item["quantity"]
        total += item_total
    
    total = math.floor(total * 100) / 100
    
    return {
        "cart_items": cart_items,
        "total": total
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)