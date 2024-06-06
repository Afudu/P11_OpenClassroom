
def test_logout(client):
    """Test logout functionality"""
    response = client.get('/logout')
    assert response.status_code == 302
    response = client.get('/')
    assert b'Welcome to the GUDLFT Registration Portal!' in response.data
