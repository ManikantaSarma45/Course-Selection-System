import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# Test to create a new course
def test_create_course():
    response = client.post(
        "/courses/",
        json={
            "name": "Data Structures",
            "course_type": "Theory"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Data Structures"
    assert data["course_type"] == "Theory"
    assert "id" in data

# Test to get a course by ID
def test_get_course():
    # First, create a course
    response = client.post(
        "/courses/",
        json={
            "name": "Operating Systems",
            "course_type": "Theory"
        }
    )
    course_id = response.json()["id"]

    # Now retrieve the course by ID
    response = client.get(f"/courses/{course_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Operating Systems"
    assert data["course_type"] == "Theory"
