
def test_successful_booking_reduces_club_points(client, mock_clubs, mock_future_competitions):
    """Test successful booking of places"""
    response = client.post('/purchasePlaces', data={
        'competition': mock_future_competitions[0]["name"],
        'club': mock_clubs[0]["name"],
        'places': '1'
    })
    assert response.status_code == 200
    new_club_points = str(int(mock_clubs[0]["points"]) - 1)
    mock_clubs[0]["points"] = new_club_points
