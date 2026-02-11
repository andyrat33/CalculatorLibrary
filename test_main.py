"""
API tests for the FastAPI calculator application.
"""
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


class TestAPI:
    def test_health(self):
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json() == {"status": "ok"}

    def test_add(self):
        response = client.get("/add", params={"a": 2, "b": 3})
        assert response.status_code == 200
        assert response.json() == {"result": 5.0}

    def test_subtract(self):
        response = client.get("/subtract", params={"a": 10, "b": 4})
        assert response.status_code == 200
        assert response.json() == {"result": 6.0}

    def test_multiply(self):
        response = client.get("/multiply", params={"a": 3, "b": 5})
        assert response.status_code == 200
        assert response.json() == {"result": 15.0}

    def test_divide(self):
        response = client.get("/divide", params={"a": 10, "b": 2})
        assert response.status_code == 200
        assert response.json() == {"result": 5}

    def test_divide_by_zero(self):
        response = client.get("/divide", params={"a": 10, "b": 0})
        assert response.status_code == 400
        assert "Cannot divide by zero" in response.json()["detail"]

    def test_divide_fl(self):
        response = client.get("/divide_fl", params={"a": 7, "b": 2})
        assert response.status_code == 200
        assert response.json() == {"result": 3.5}

    def test_divide_fl_by_zero(self):
        response = client.get("/divide_fl", params={"a": 7, "b": 0})
        assert response.status_code == 400
        assert "Cannot divide by zero" in response.json()["detail"]

    def test_square(self):
        response = client.get("/square", params={"a": 5})
        assert response.status_code == 200
        assert response.json() == {"result": 25.0}

    def test_cube(self):
        response = client.get("/cube", params={"a": 3})
        assert response.status_code == 200
        assert response.json() == {"result": 27.0}

    def test_power(self):
        response = client.get("/power", params={"a": 2, "b": 10})
        assert response.status_code == 200
        assert response.json() == {"result": 1024.0}

    def test_mod(self):
        response = client.get("/mod", params={"a": 10, "b": 3})
        assert response.status_code == 200
        assert response.json() == {"result": 1.0}

    def test_mod_by_zero(self):
        response = client.get("/mod", params={"a": 10, "b": 0})
        assert response.status_code == 400
        assert "Cannot divide by zero" in response.json()["detail"]

    def test_square_root(self):
        response = client.get("/square_root", params={"a": 16})
        assert response.status_code == 200
        assert response.json() == {"result": 4.0}

    def test_itob(self):
        response = client.get("/itob", params={"a": 10})
        assert response.status_code == 200
        assert response.json() == {"result": "0b1010"}
