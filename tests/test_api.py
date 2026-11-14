"""
Pruebas de endpoints REST (GET, POST y DELETE).

"""
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_api_get_users():
    respuesta = requests.get(f"{BASE_URL}/users/1")
    assert respuesta.status_code == 200
    datos = respuesta.json()
    assert datos["id"] == 1
    assert "username" in datos

def test_api_post_resource():
    nuevo_post = {
        "title": "Entrega Final QA - Erika Silverio",
        "body": "Automatizacion de API con Requests",
        "userId": 1
    }
    respuesta = requests.post(f"{BASE_URL}/posts", json=nuevo_post)
    assert respuesta.status_code == 201
    datos = respuesta.json()
    assert datos["title"] == "Entrega Final QA - Erika Silverio"
    assert "id" in datos

def test_api_delete_resource():
    respuesta = requests.delete(f"{BASE_URL}/posts/1")
    assert respuesta.status_code in [200, 204]