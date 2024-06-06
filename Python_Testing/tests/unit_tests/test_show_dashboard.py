
def test_show_dashboard(client, mock_clubs):
    """Test that the dashboard page loads properly."""
    response = client.get('/dashBoard')
    assert response.status_code == 200
    assert b'GUDLFT Dashboard' in response.data
    assert f'{mock_clubs[0]["name"]}' in str(response.data)
    assert f'{mock_clubs[0]["points"]}' in str(response.data)
    assert b'Back to Home' in response.data
