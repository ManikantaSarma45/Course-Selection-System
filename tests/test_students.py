import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# Test to create a new student
def test_create_student():
    response = client.post(
        "/students/",
        json={"name": "John Doe", "email": "john.doe@example.com"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "John Doe"
    assert data["email"] == "john.doe@example.com"
    assert "id" in data

# Test to get a student by ID
def test_get_student():
    # First, create a student
    response = client.post(
        "/students/",
        json={"name": "Jane Doe", "email": "jane.doe@example.com"}
    )
    student_id = response.json()["id"]

    # Now retrieve the student by ID
    response = client.get(f"/students/{student_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Jane Doe"
    assert data["email"] == "jane.doe@example.com"
