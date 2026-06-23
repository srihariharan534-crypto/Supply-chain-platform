from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(
    title="Supply Chain Platform API",
    description="End-to-End Analytics and Intelligence API for Supply Chain Management",
    version="1.0.0"
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Supply Chain Platform API"}

# Simple placeholder routes to satisfy requirements
@app.get("/api/v1/inventory")
def get_inventory():
    return {"status": "success", "data": "Inventory data placeholder"}

@app.get("/api/v1/logistics")
def get_logistics():
    return {"status": "success", "data": "Logistics data placeholder"}

@app.get("/api/v1/suppliers")
def get_suppliers():
    return {"status": "success", "data": "Supplier data placeholder"}

@app.get("/api/v1/warehouse")
def get_warehouse():
    return {"status": "success", "data": "Warehouse data placeholder"}

@app.get("/api/v1/executive")
def get_executive():
    return {"status": "success", "data": "Executive data placeholder"}
