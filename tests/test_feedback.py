import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# Test to submit feedback for a teacher
def test_submit_feedback():
    # Create a student and a teacher first
    student_response = client.post(
        "/students/",
        json={"name": "John Doe", "email": "john.doe@example.com"}
    )
    teacher_response = client.post(
        "/teachers/",
        json={
            "name": "Dr. Alice Smith",
            "academic_background": "Ph.D. in Computer Science",
            "research_projects": "AI, Machine Learning",
            "patents": "AI optimization methods"
        }
    )
    student_id = student_response.json()["id"]
    teacher_id = teacher_response.json()["id"]

    # Now submit feedback
    feedback_response = client.post(
        "/feedback/",
        json={
            "student_id": student_id,
            "teacher_id": teacher_id,
            "feedback_text": "Great professor!",
            "rating": 5
        }
    )
    assert feedback_response.status_code == 200
    feedback_data = feedback_response.json()
    assert feedback_data["feedback_text"] == "Great professor!"
    assert feedback_data["rating"] == 5
    assert "id" in feedback_data
