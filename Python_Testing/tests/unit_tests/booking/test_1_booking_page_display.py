
def test_booking_page_display(client, mock_clubs, mock_competitions):
    """Test that booking page is displayed correctly when booking a competition."""
    # testing with the second competition in the competition test data list.
    response = client.get(f'/book/{mock_competitions[1]["name"]}/{mock_clubs[0]["name"]}')
    assert response.status_code == 200
    assert b"How many places?" in response.data
    assert f'{mock_competitions[1]["name"]}' in str(response.data)
