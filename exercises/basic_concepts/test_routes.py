import sys
import os
import pytest

# Añadimos la raíz del proyecto al path
root_path = os.path.abspath(os.path.dirname(__file__))
if root_path not in sys.path:
    sys.path.insert(0, root_path)

# Importa la app Flask desde routes.py
from exercises.basic_concepts.controller.routes import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    data = response.data.decode('utf-8')
    assert "Buscar" in data or "form" in data

def test_users_page(client):
    response = client.get('/users')
    assert response.status_code == 200
    data = response.data.decode('utf-8')
    assert "Usuarios" in data or "result" in data

def test_search_by_id_invalid(client):
    response = client.post('/search', data={'search_type': 'id', 'query': 'abc'})
    assert response.status_code == 200
    data = response.data.decode('utf-8')
    assert "El ID debe ser un número válido" in data
