import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# Test to create a new teacher
def test_create_teacher():
    response = client.post(
        "/teachers/",
        json={
            "name": "Dr. Alice Smith",
            "academic_background": "Ph.D. in Computer Science",
            "research_projects": "AI, Machine Learning",
            "patents": "AI optimization methods"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Dr. Alice Smith"
    assert data["academic_background"] == "Ph.D. in Computer Science"
    assert "id" in data

# Test to get a teacher by ID
def test_get_teacher():
    # First, create a teacher
    response = client.post(
        "/teachers/",
        json={
            "name": "Dr. Bob Johnson",
            "academic_background": "Ph.D. in Mathematics",
            "research_projects": "Cryptography",
            "patents": "Encryption methods"
        }
    )
    teacher_id = response.json()["id"]

    # Now retrieve the teacher by ID
    response = client.get(f"/teachers/{teacher_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Dr. Bob Johnson"
    assert data["academic_background"] == "Ph.D. in Mathematics"
