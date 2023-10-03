from app import app

import pytest

#test index page
def test_index_page():
    with app.test_client() as client:
        response = client.get('/')
    assert response.status_code == 200
    assert b'Your assistant, Staying side by side whenever you need it' in response.data
 
 #test register page   
def test_register_page():
    with app.test_client() as client:
        response = client.get('/register_page/')
    assert response.status_code == 200
    assert b'login to Chatty' in response.data

#error handling   
def test_login_page():
    with app.test_client() as client:
        response = client.get('/login_page/')
    assert response.status_code == 200
    assert b'Start using Chatty' in response.data
    
def test_error_handling():
    with app.test_client() as client:
        response = client.get('/nonexistent_route')
        assert response.status_code == 404
        
    data = {'username': '', 'password': ''}
    response = client.post('/chat_view/', data=data, follow_redirects=True)
    assert response.status_code ==400
    assert('Invalid form submission', response.data.decode())
    

        
    

    