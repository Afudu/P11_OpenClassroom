
def test_login_valid_email(client, mock_clubs):
    """Test successful login with a valid email."""
    response = client.post('/showSummary', data={'email': mock_clubs[0]['email']})
    assert response.status_code == 200
    assert f'Welcome, {mock_clubs[0]["email"]}' in str(response.data)


def test_login_invalid_email(client):
    """Test login failure with an unknown email."""
    response = client.post('/showSummary', data={'email': 'invalid@example.com'})
    assert response.status_code == 302  # should redirect
    assert b'That email was not found in the database.' in client.get('/').data
