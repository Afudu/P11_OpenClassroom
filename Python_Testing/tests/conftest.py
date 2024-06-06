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

