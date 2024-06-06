"""
This file contains setup functions called fixtures that the tests will use.
"""
import pytest
from Python_Testing import server
from datetime import datetime, timedelta

# Calculate the date for next week
next_week_date = datetime.today() + timedelta(weeks=1)
next_week_date = next_week_date.strftime('%Y-%m-%d %H:%M:%S')

# Calculate the date for next week
next_month_date = datetime.today() + timedelta(weeks=4)
next_month_date = next_month_date.strftime('%Y-%m-%d %H:%M:%S')

# Calculate the date for last week
last_week_date = datetime.today() - timedelta(weeks=1)
last_week_date = last_week_date.strftime('%Y-%m-%d %H:%M:%S')


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


@pytest.fixture
def mock_past_competitions():
    competitions = server.competitions = [
        {
            "name": "Test Festival Leixlip",
            "date": last_week_date,
            "numberOfPlaces": "25"
        }
    ]
    yield competitions


@pytest.fixture
def mock_future_competitions():
    competitions = server.competitions = [
        {
            "name": "Test - Spring Festival",
            "date": next_week_date,
            "numberOfPlaces": "25"
        },
        {
            "name": "Test - Fall Classic",
            "date": next_month_date,
            "numberOfPlaces": "4"
        }
    ]
    yield competitions
