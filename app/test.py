from fastapi.testclient import TestClient
from main import app, CreateItemRequest, UpdateItemRequest

client = TestClient(app)


def test_create_item():
    response = client.post(url="/items", json=CreateItemRequest(
        name="Steak",
        description="Delicious steak",
        price=10.0,
        tax=1.5).model_dump())
    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.json()["name"] == "Steak"
    assert response.json()["description"] == "Delicious steak"
    assert float(response.json()["price"]) == 10.0
    assert float(response.json()["tax"]) == 1.5

    response = client.post(url="/items", json=CreateItemRequest(
        name="Bread",
        description="Delicious bread",
        price=3.0,
        tax=0.5).model_dump())
    assert response.status_code == 200
    assert response.json()["id"] == 2
    assert response.json()["name"] == "Bread"
    assert response.json()["description"] == "Delicious bread"
    assert float(response.json()["price"]) == 3.0
    assert float(response.json()["tax"]) == 0.5

    response = client.post(url="/items", json=CreateItemRequest(
        name="Apple",
        description="Delicious apple",
        price=2.0,
        tax=0.4).model_dump())
    assert response.status_code == 200
    assert response.json()["id"] == 3
    assert response.json()["name"] == "Apple"
    assert response.json()["description"] == "Delicious apple"
    assert float(response.json()["price"]) == 2.0
    assert float(response.json()["tax"]) == 0.4


def test_get_items():
    response = client.get(url="/items")
    assert response.status_code == 200
    assert response.json()[0]["id"] == 1
    assert response.json()[0]["name"] == "Steak"
    assert response.json()[0]["description"] == "Delicious steak"
    assert float(response.json()[0]["price"]) == 10.0
    assert float(response.json()[0]["tax"]) == 1.5

    assert response.json()[1]["id"] == 2
    assert response.json()[1]["name"] == "Bread"
    assert response.json()[1]["description"] == "Delicious bread"
    assert float(response.json()[1]["price"]) == 3.0
    assert float(response.json()[1]["tax"]) == 0.5

    assert response.json()[2]["id"] == 3
    assert response.json()[2]["name"] == "Apple"
    assert response.json()[2]["description"] == "Delicious apple"
    assert float(response.json()[2]["price"]) == 2.0
    assert float(response.json()[2]["tax"]) == 0.4


def test_get_item():
    response = client.get(url="/items/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.json()["name"] == "Steak"
    assert response.json()["description"] == "Delicious steak"
    assert float(response.json()["price"]) == 10.0
    assert float(response.json()["tax"]) == 1.5

    response = client.get(url="/items/2")
    assert response.status_code == 200
    assert response.json()["id"] == 2
    assert response.json()["name"] == "Bread"
    assert response.json()["description"] == "Delicious bread"
    assert float(response.json()["price"]) == 3.0
    assert float(response.json()["tax"]) == 0.5

    response = client.get(url="/items/3")
    assert response.status_code == 200
    assert response.json()["id"] == 3
    assert response.json()["name"] == "Apple"
    assert response.json()["description"] == "Delicious apple"
    assert float(response.json()["price"]) == 2.0
    assert float(response.json()["tax"]) == 0.4


def test_update_item():
    response = client.put(url="/items/3", json=UpdateItemRequest(
        name="Orange",
        description="Delicious orange",
        price=2.5,
        tax=0.6).model_dump())
    assert response.status_code == 200
    assert response.json()["id"] == 3
    assert response.json()["name"] == "Orange"
    assert response.json()["description"] == "Delicious orange"
    assert float(response.json()["price"]) == 2.5
    assert float(response.json()["tax"]) == 0.6

    response = client.get(url="/items/3")
    assert response.status_code == 200
    assert response.json()["id"] == 3
    assert response.json()["name"] == "Orange"
    assert response.json()["description"] == "Delicious orange"
    assert float(response.json()["price"]) == 2.5
    assert float(response.json()["tax"]) == 0.6


def test_delete_item():
    response = client.delete(url="/items/2")
    assert response.status_code == 200
    assert response.json()["id"] == 2
    assert response.json()["name"] == "Bread"
    assert response.json()["description"] == "Delicious bread"
    assert float(response.json()["price"]) == 3.0
    assert float(response.json()["tax"]) == 0.5

    response = client.get(url="/items")
    assert response.status_code == 200
    assert response.json()[0]["id"] == 1
    assert response.json()[0]["name"] == "Steak"
    assert response.json()[0]["description"] == "Delicious steak"
    assert float(response.json()[0]["price"]) == 10.0
    assert float(response.json()[0]["tax"]) == 1.5

    response = client.get(url="/items")
    assert response.status_code == 200
    assert response.json()[1]["id"] == 3
    assert response.json()[1]["name"] == "Orange"
    assert response.json()[1]["description"] == "Delicious orange"
    assert float(response.json()[1]["price"]) == 2.5
    assert float(response.json()[1]["tax"]) == 0.6

