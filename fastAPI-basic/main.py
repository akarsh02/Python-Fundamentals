from fastapi import FastAPI

app = FastAPI()

@app.get("/") #no routes will be repeated in entire project
def home():
    return { "Welcome to the FastAPI application!"}

@app.get("/contact") 
def contact():
    return {"You can reach us at..."}