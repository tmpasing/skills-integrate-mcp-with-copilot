import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_student_login_success():
    response = client.post(
        "/auth/login",
        json={
            "role": "student",
            "email": "michael@mergington.edu",
            "password": "student123",
        },
    )

    assert response.status_code == 200
    data = response.json()
    assert data["role"] == "student"
    assert data["email"] == "michael@mergington.edu"
    assert "token" in data


def test_invalid_login_fails():
    response = client.post(
        "/auth/login",
        json={
            "role": "student",
            "email": "michael@mergington.edu",
            "password": "wrong-password",
        },
    )

    assert response.status_code == 401


def test_advisor_login_success():
    response = client.post(
        "/auth/login",
        json={
            "role": "advisor",
            "email": "coach@mergington.edu",
            "password": "advisor123",
        },
    )

    assert response.status_code == 200
    data = response.json()
    assert data["role"] == "advisor"
    assert data["email"] == "coach@mergington.edu"
    assert "token" in data
