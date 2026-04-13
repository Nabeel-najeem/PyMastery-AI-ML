from fastapi import FastAPI
from model import products as pd


app = FastAPI()

product = [
    pd(id=1,product_name="phone",description= "budget phone",price = 20000.0,quantity=10),
    pd(id=2,product_name="laptop",description= "budget laptop",price = 45000.0,quantity=12),
    pd(id=3,product_name="fan",description= "budget fan",price = 7000.0,quantity=9),
    pd(id=4,product_name="car",description= "budget car",price = 200000.0,quantity=7),
    
]

@app.get("/")
def greet():
    return "Welcome to my shope"

@app.get("/all_products")
def all_products():
    return product

@app.get("/product/{id}")
def get_product_id(id : int):
    for item in product :
        if item.id == id :
            return item
        
    return "product not found"