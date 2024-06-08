def test_booking_more_than_club_points(client, mock_clubs, mock_competitions):
    """Test booking more places than the club's points."""
    # test with club having 4 points and booking 5 places
    response = client.post('/purchasePlaces', data={
        'competition': mock_competitions[1]["name"],
        'club': mock_clubs[1]["name"],
        'places': "5"
    })
    assert response.status_code == 200
    assert b"You do not have enough points to book this number of places." in response.data
