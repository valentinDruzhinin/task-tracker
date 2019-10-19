from flask import request, current_app, make_response, redirect, url_for, Response, render_template
from app.status_codes import BAD_REQUEST


def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = current_app.pass_encoder(request.form.get('password', '').encode()).hexdigest()
        user_info = current_app.users_repository.query(email=email, password=password)[0]
        if user_info:
            resp = make_response(redirect(url_for('users', user_id=user_info.id)))
            resp.set_cookie('email', current_app.signer.sign(email))
            return resp
        return Response('Unable to login. Wrong credentials provided.', status=BAD_REQUEST)
    return render_template('login.html')
