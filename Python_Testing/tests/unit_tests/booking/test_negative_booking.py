
def test_negative_booking(client, mock_clubs, mock_future_competitions):
    """Test booking a negative number of places."""
    response = client.post('/purchasePlaces', data={
        'competition': mock_future_competitions[0]["name"],
        'club': mock_clubs[0]["name"],
        'places': "-1"
    })
    assert response.status_code == 200
    assert b"You cannot book negative competition places." in response.data
