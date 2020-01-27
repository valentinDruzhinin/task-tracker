def test_pass():
  pass


# @pytest.mark.parametrize('path,result', [
#     ('/register', '<form method="post" action="/register">'),
#     ('/login', '<form method="post" action="/login">')
# ])
# def test_pages_loading(path, result):
#     response = client.get(path, follow_redirects=True)
#
#     assert response.status == '200 OK'
#     assert result in response.data.decode()
#
#
# def test_register_login(db_fixture):
#     # register and login user
#     response = client.post('/register', data=USER, follow_redirects=True)
#     assert response.status == '200 OK'
#     assert db_fixture.execute(SQLQuery.HAS_USER, (USER['email'],)).fetchone()
#
#     # fail to register user with the same email
#     response = client.post('/register', data=USER, follow_redirects=True)
#     assert response.status == '409 CONFLICT'
#     assert 'User already exist' == response.data.decode()
#
#     # login user
#     response = client.post('/login', data=USER, follow_redirects=True)
#     assert response.status == '200 OK'
#
#     # fail to login user
#     # user_with_wrong_email = copy(USER)
#     # user_with_wrong_email['email'] = 'wrong_email@test'
#     user_with_wrong_email = {**USER, 'email': 'wrong_email@test'}
#     response = client.post('/login', data=user_with_wrong_email, follow_redirects=True)
#     assert response.status == '400 BAD REQUEST'
#     assert 'Unable to login. Wrong credentials provided.' == response.data.decode()
#
#     user_with_wrong_password = copy(USER)
#     user_with_wrong_password['password'] = 'wrong_password'
#     response = client.post('/login', data=user_with_wrong_password, follow_redirects=True)
#     assert response.status == '400 BAD REQUEST'
#     assert 'Unable to login. Wrong credentials provided.' == response.data.decode()
