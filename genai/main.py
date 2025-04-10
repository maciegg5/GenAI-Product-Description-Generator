from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import random
import json
import os

app = FastAPI(title="AI-Powered E-commerce Assistant")

PRODUCTS_FILE = "products.json"

# Models
class ProductRequest(BaseModel):
    name: str
    category: str

class Product(BaseModel):
    name: str
    category: str
    description: str

# Simulated AI description generator
def generate_description(name: str, category: str) -> str:
    templates = [
        f"Discover the all-new {name}, the ultimate choice for anyone in need of premium-quality {category}.",
        f"The {name} redefines what {category} should feel like – comfort, performance, and style combined.",
        f"Step up your game with {name}, your go-to {category} for any occasion."
    ]
    return random.choice(templates)

# File helpers
def load_products() -> List[Product]:
    if not os.path.exists(PRODUCTS_FILE):
        return []
    with open(PRODUCTS_FILE, "r") as f:
        return [Product(**item) for item in json.load(f)]

def save_products(products: List[Product]):
    with open(PRODUCTS_FILE, "w") as f:
        json.dump([product.dict() for product in products], f, indent=2)

# Routes
@app.post("/generate-description", response_model=Product)
def create_description(product: ProductRequest):
    description = generate_description(product.name, product.category)
    return Product(name=product.name, category=product.category, description=description)

@app.post("/products", response_model=Product)
def add_product(product: ProductRequest):
    description = generate_description(product.name, product.category)
    new_product = Product(name=product.name, category=product.category, description=description)
    products = load_products()
    products.append(new_product)
    save_products(products)
    return new_product

@app.get("/products", response_model=List[Product])
def list_products():
    return load_products()

@app.get("/products/{category}", response_model=List[Product])
def get_products_by_category(category: str):
    products = load_products()
    filtered = [p for p in products if p.category.lower() == category.lower()]
    if not filtered:
        raise HTTPException(status_code=404, detail=f"No products found in category '{category}'")
    return filtered