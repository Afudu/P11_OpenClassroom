"""
This file contains setup functions called fixtures that the tests will use.
"""
import pytest
from Python_Testing import server


@pytest.fixture
def client():
    """A test client for the app."""
    server.app.config['TESTING'] = True
    client = server.app.test_client()
    yield client


@pytest.fixture
def mock_clubs():
    clubs = server.clubs = [
        {
            "name": "Simply Lift",
            "email": "john@simplylift.co",
            "points": "13"
        },
        {
            "name": "Iron Temple",
            "email": "admin@irontemple.com",
            "points": "4"
        },
    ]
    yield clubs
