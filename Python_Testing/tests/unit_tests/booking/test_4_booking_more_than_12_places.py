
def test_booking_more_than_12_places(client, mock_clubs, mock_future_competitions):
    """Test booking more places than 12 places."""
    response = client.post('/purchasePlaces', data={
        'competition': mock_future_competitions[0]["name"],
        'club': mock_clubs[0]["name"],
        'places': "13"
    })
    assert response.status_code == 200
    assert b"You cannot book more than 12 places" in response.data
