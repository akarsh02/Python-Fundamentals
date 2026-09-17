from fastapi import FastAPI,Request
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


#####Passing data from client to server using path and query params

## Path Params..
@app.get("/products/{product_id}")
def get_one_product(product_id: int):
    for id in products:
        if id["id"] == product_id:
            return id
        else:
            return {"message": "Product not found!"}


## Query Params..
@app.get("/greet")
def greet_user(request:Request):         ##request for n number of data from client to server using query params
    query_params = request.query_params
    name = query_params.get("name")
    age = query_params.get("age")
    return f"Hello, {name}! You are {age} years old."