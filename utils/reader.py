"""
Funciones auxiliares para leer los datos de prueba desde CSV y JSON.

"""
import csv
import json

def read_users_csv():
    with open("data/users.csv", newline="", encoding="utf-8") as archivo:
        return list(csv.DictReader(archivo))

def read_productos_json():
    with open("data/products.json", encoding="utf-8") as archivo:
        return json.load(archivo)