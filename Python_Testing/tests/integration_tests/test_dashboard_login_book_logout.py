def test_dashboard_login_book_logout(client, mock_clubs, mock_competitions, mock_save_json):
    """Test that the secretary performs several actions as expected."""

    # 1 - the secretary of 1st club in test data  visits the home page which is online
    response = client.get("/")
    assert response.status_code == 200
    assert b'Welcome to the GUDLFT Registration Portal!' in response.data
    assert b'Please enter your secretary email' in response.data

    # 2 - then visits the dashboard page to check the club points
    response = client.get('/dashBoard')
    assert response.status_code == 200
    assert b'GUDLFT Dashboard' in response.data
    assert b'Back to Home' in response.data

    # 3 - then returns to the home page
    response = client.get("/")
    assert response.status_code == 200
    assert b'Welcome to the GUDLFT Registration Portal!' in response.data
    assert b'Please enter your secretary email' in response.data

    # 4 - then logs in using the club's email
    response = client.post('/showSummary', data={'email': mock_clubs[0]['email']})
    assert response.status_code == 200
    assert f'Welcome, {mock_clubs[0]["email"]}' in str(response.data)

    # 5 - then books a place in one of the upcoming events
    response = client.post('/purchasePlaces', data={
        'competition': mock_competitions[1]["name"],
        'club': mock_clubs[0]["name"],
        'places': '1'
    })
    assert response.status_code == 200
    assert b'Great-booking complete!' in response.data

    # then logs out
    response = client.get('/logout')
    assert response.status_code == 302
    response = client.get('/')
    assert b'Welcome to the GUDLFT Registration Portal!' in response.data
