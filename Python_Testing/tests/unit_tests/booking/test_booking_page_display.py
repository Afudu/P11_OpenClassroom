
def test_booking_page_display(client, mock_clubs, mock_future_competitions):
    """Test that booking page is displayed correctly when booking a competition."""
    response = client.get(f'/book/{mock_future_competitions[0]["name"]}/{mock_clubs[0]["name"]}')
    assert response.status_code == 200
    assert b"How many places?" in response.data
    assert f'{mock_future_competitions[0]["name"]}' in str(response.data)
