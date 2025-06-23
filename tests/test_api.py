import pytest
from fastapi.testclient import TestClient

from init_db import init_db
from main import app

client = TestClient(app)

@pytest.fixture(autouse=True)
def setup_db():
    # Initialize the database before each test
    init_db()
    yield
    # Optionally reinitialize or clean up after tests
    init_db()

def test_get_users_default_pagination():
    # Default should return first page with default page_size (10)
    response = client.get("/api/users")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    # Expect default page size of 10 users
    assert len(data) == 10

def test_get_users_custom_pagination():
    # Request second page with 5 items per page
    response = client.get("/api/users?page=2&page_size=5")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    # Should return 5 users on page 2
    assert len(data) == 5
    # Confirm items are consecutive (ids 6-10)
    ids = [u['id'] for u in data]
    assert ids == list(range(6, 11))

def test_search_users():
    # Search for a known last name
    response = client.get("/api/users?search=hansen")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    # All returned users should have 'hansen' in their first or last name or email
    for u in data:
        full = f"{u['first_name']} {u['last_name']}".lower()
        assert 'hansen' in full or 'hansen' in u['email'].lower()

def test_create_user():
    # Create a new user via POST
    new_user = {
        "first_name": "Test",
        "last_name": "User",
        "email": "test.user@example.com"
    }
    response = client.post("/api/users", json=new_user)
    # Expect creation success (201 Created)
    assert response.status_code == 201
    created = response.json()
    # Response should include assigned id and match sent data
    assert 'id' in created
    assert created['first_name'] == new_user['first_name']
    assert created['last_name'] == new_user['last_name']
    assert created['email'] == new_user['email']

    # Verify new user appears in search results
    resp2 = client.get("/api/users?search=test.user@example.com")
    assert resp2.status_code == 200
    results = resp2.json()
    assert any(u['email'] == new_user['email'] for u in results)