from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from services import ProductService

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

service = ProductService()

@app.get("/")
def read_root():
    return FileResponse('../front/index.html')

@app.post("/products")
def create_product(name: str, price: float):
    return service.create_product(name, price)

@app.get("/products")
def get_products():
    return service.get_products()

@app.get("/products/highest")
def get_highest():
    return service.get_highest_price()

@app.get("/products/lowest")
def get_lowest():
    return service.get_lowest_price()

@app.get("/products/average")
def get_average():
    return service.get_average_price()

@app.get("/products/above-average")
def get_above_average():
    return service.get_above_average()

@app.get("/products/below-average")
def get_below_average():
    return service.get_below_average()

@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    return service.delete_product(product_id)