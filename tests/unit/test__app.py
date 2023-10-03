from app.model import User, Chat,db


def test_validate_user():
    user = User(1, "username","email@gmai.com","2023-05-14 12:47:02.567748","user","123" )
     
    assert user.username == "username"
    assert user.email == "email@gmai.com"
    assert user.name == "user"
    
def test_validate_chat():
    chat =Chat(
    id = 1,
    question = "question 1",
    answer = "answer 1",
    timestamp ="2023-05-14 12:47:02.567748",
    user_id = 1
            
    )
    
    assert chat.question == "question 1"
    assert chat.answer == "answer 1"
    assert chat.timestamp == "2023-05-14 12:47:02.567748"
    
    
def test_login_success(self):
    # Send a POST request with valid login data
    response = self.app.post('/chat_view/', data={
        'name': 'John Doe',
        'email': 'john@example.com',
        'username': 'johndoe',
        'password': 'password123'
    })
    # Assert that the response status code is 200 and the login.html template is rendered
    self.assertEqual(response.status_code, 200)
    self.assertIn(b'Login Successful', response.data)
