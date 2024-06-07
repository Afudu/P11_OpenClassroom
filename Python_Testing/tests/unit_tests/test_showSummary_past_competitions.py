
def test_showSummary_past_competitions_no_booking_link(client, mock_clubs, mock_past_competitions):
    """Test that after login, a past competition does not display Booking link,
    preventing to book past competitions."""
    response = client.post('/showSummary', data={"email": mock_clubs[0]["email"]})
    assert response.status_code == 200
    # assert f'{mock_past_competitions[0]["name"]}' in str(response.data)
    assert b'Logout' in response.data
    assert b'Competitions' in response.data
    assert b'Book Places' not in response.data
