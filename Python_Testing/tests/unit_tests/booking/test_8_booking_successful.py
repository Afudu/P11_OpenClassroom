def test_successful_booking_reduces_club_points(client, mock_clubs, mock_competitions, mock_save_json):
    """Test successful booking of places"""
    response = client.post('/purchasePlaces', data={
        'competition': mock_competitions[1]["name"],
        'club': mock_clubs[0]["name"],
        'places': '1'
    })
    assert response.status_code == 200
    assert b'Great-booking complete!' in response.data
