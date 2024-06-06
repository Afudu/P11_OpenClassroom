
def test_index_url_online(client):
    """Test that the index page loads properly."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to the GUDLFT Registration Portal!' in response.data
