from fastapi import FastAPI
from mockData import products

app = FastAPI()

@app.get("/") #no routes will be repeated in entire project
def home():
    return { "Welcome to the FastAPI application!"}

@app.get("/contact") 
def contact():
    return {"You can reach us at..."}

@app.get("/products")
def get_products():
    return products



## Path Params..
@app.get("/products/{product_id}")
def get_one_product(product_id: int):
    for id in products:
        if id["id"] == product_id:
            return id
        else:
            return {"message": "Product not found!"}


