
def test_zero_booking(client, mock_clubs, mock_competitions):
    """Test booking zero."""
    response = client.post('/purchasePlaces', data={
        'competition': mock_competitions[1]["name"],
        'club': mock_clubs[0]["name"],
        'places': "0"
    })
    assert response.status_code == 200
    assert b"Please chose a number between 1 and 12" in response.data
