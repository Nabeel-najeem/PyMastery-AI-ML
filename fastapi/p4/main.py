from fastapi import FastAPI,Depends
from model import product
from database import Session,engine
import database_model
from sqlalchemy.orm import Session as dbsession
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["http://localhost:3000"],
    allow_methods = ["*"]
)


database_model.Base.metadata.create_all(bind = engine)

products = [
    product(id=1,product_name="phone",description= "budget phone",price = 20000.0,quantity=10),
    product(id=2,product_name="laptop",description= "budget laptop",price = 45000.0,quantity=12),
    product(id=3,product_name="fan",description= "budget fan",price = 7000.0,quantity=9),
    product(id=4,product_name="car",description= "budget car",price = 200000.0,quantity=7),   
]

def get_db():
    db = Session()
    try :
        yield db
    finally :
        db.close()

def init_db():
    
    db = Session()
    count = db.query(database_model.product).count()
    if count == 0 :
        for product in products :
            db.add(database_model.product(**product.model_dump()))
        db.commit()
    
init_db()

@app.get("/")
def greet():
    return "Welcome to my shope"
#get all products
@app.get("/products")
def all_products(db : dbsession = Depends(get_db)):
    
    db_products = db.query(database_model.product).all()
    return db_products
#fetch product by id
@app.get("/product/{id}")
def get_product_id(id : int, db : dbsession = Depends(get_db)):
    db_product = db.query(database_model.product).filter(database_model.product.id == id).first()
    if db_product :
        return db_product
    return "product not found"

#add new product     
@app.post("/products")
def add_product(product : product, db : dbsession = Depends(get_db)):
    db.add(database_model.product(**product.model_dump()))
    db.commit()
    return product

#update product by id
@app.put("/products/{id}")
def update_product(id : int , product : product, db : dbsession = Depends(get_db)):
    db_product = db.query(database_model.product).filter(database_model.product.id == id).first()
    if db_product :
        db_product.product_name = product.product_name
        db_product.description = product.description
        db_product.price = product.price
        db_product.quantity = product.quantity
        db.commit()
        return "product updated sussefully"  
    else :
        return "No product found"
   
#delete product by id
@app.delete("/products/{id}")
def del_product(id :int, db : dbsession = Depends(get_db)):
    db_product = db.query(database_model.product).filter(database_model.product.id == id).first()
    if db_product :
        db.delete(db_product)    
        db.commit()
        return "product deleted sucesfully"  
    else :
        return "product not found"
    
