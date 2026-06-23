import logging
from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()

def test_inventory_endpoint():
    response = client.get("/api/v1/inventory")
    assert response.status_code == 200
    assert response.json()["status"] == "success"

def test_logistics_endpoint():
    response = client.get("/api/v1/logistics")
    assert response.status_code == 200
    assert response.json()["status"] == "success"

def test_suppliers_endpoint():
    response = client.get("/api/v1/suppliers")
    assert response.status_code == 200
    assert response.json()["status"] == "success"

def test_warehouse_endpoint():
    response = client.get("/api/v1/warehouse")
    assert response.status_code == 200
    assert response.json()["status"] == "success"
