"""
This file contains setup functions called fixtures that the tests will use.
"""
import pytest
from Python_Testing import server
from Python_Testing.tests import testing_data


@pytest.fixture
def client():
    """A test client for the app."""
    server.app.config['TESTING'] = True
    client = server.app.test_client()
    yield client


#
@pytest.fixture
def mock_clubs():
    # mock_clubs_data() simulates clubs in server
    server.clubs = testing_data.clubs_test_data()
    return server.clubs


@pytest.fixture
def mock_competitions():
    server.competitions = testing_data.competitions_test_data()
    return server.competitions


@pytest.fixture
def mock_past_competitions():
    server.competitions = [testing_data.competitions_test_data()[0]]
    return server.competitions


# @pytest.fixture
# def mock_save_json(mocker):
#     return mocker.patch('server.saveJson', side_effect=lambda x, y: None)

@pytest.fixture
def mock_save_json():
    """
    Prevents test data to be saved in the json file
    to preserve file integrity after tests.
    """
    server.saveJson = lambda x, y: None
    return server.saveJson

# @pytest.fixture
# def mock_save_data(monkeypatch):
#     def mock_save_clubs():
#         pass
#
#     def mock_save_competitions():
#         pass
#
#     monkeypatch.setattr('server.saveClubs', mock_save_clubs)
#     monkeypatch.setattr('server.saveCompetitions', mock_save_competitions)
