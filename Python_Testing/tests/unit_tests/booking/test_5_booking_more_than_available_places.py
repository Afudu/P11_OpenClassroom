def test_booking_more_than_available_places(client, mock_clubs, mock_competitions):
    """Test booking more places than available competition places."""
    # testing with the 3rd competition in the competition test data that has 4 places.
    response = client.post('/purchasePlaces', data={
        'competition': mock_competitions[2]["name"],
        'club': mock_clubs[0]["name"],
        'places': "5"
    })
    assert response.status_code == 200
    assert b"You cannot book more than there are places available." in response.data
