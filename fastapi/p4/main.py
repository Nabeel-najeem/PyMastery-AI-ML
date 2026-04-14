from fastapi import FastAPI
from model import product
from database import Session


app = FastAPI()

products = [
    product(id=1,product_name="phone",description= "budget phone",price = 20000.0,quantity=10),
    product(id=2,product_name="laptop",description= "budget laptop",price = 45000.0,quantity=12),
    product(id=3,product_name="fan",description= "budget fan",price = 7000.0,quantity=9),
    product(id=4,product_name="car",description= "budget car",price = 200000.0,quantity=7),
    
]

@app.get("/")
def greet():
    return "Welcome to my shope"

@app.get("/products")
def all_products():
    db = Session()
    db.query()
    return products

@app.get("/product/{id}")
def get_product_id(id : int):
    for product in products :
        if product.id == id :
            return product
    return "product not found"
        
@app.post("/product")
def add_product(product : product):
    products.append(product)
    return product

@app.put("/product")
def update_product(id : int , product : product):
    for i in range(len(products)):
        if products[i].id == id :
            products[i] = product
            return "product added sussefully"
        
    return "No product found"

@app.delete("/product")
def del_product(id :int):
    for i in range(len(products)):
        if products[i].id == id :
            del products[i]
            return "product deleted sucesfully"
    return "product not found"