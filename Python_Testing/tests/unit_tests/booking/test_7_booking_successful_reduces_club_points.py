def test_successful_booking_reduces_club_points(client, mock_clubs, mock_competitions, mock_save_json):
    """Test successful booking of places"""
    # mocker.patch('server.saveJson', side_effect=lambda x, y: None)
    response = client.post('/purchasePlaces', data={
        'competition': mock_competitions[1]["name"],
        'club': mock_clubs[0]["name"],
        'places': '1'
    })
    assert response.status_code == 200
    new_club_points = str(int(mock_clubs[0]["points"]) - 1)
    mock_clubs[0]["points"] = new_club_points
