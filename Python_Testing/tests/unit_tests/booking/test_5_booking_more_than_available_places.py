
def test_booking_more_than_available_places(client, mock_clubs, mock_future_competitions):
    """Test booking more places than available competition places."""
    response = client.post('/purchasePlaces', data={
        'competition': mock_future_competitions[1]["name"],
        'club': mock_clubs[0]["name"],
        'places': "5"
    })
    assert response.status_code == 200
    assert b"You cannot book more than there are places available." in response.data
