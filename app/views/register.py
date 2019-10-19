from flask import request, current_app, Response, render_template, make_response, redirect, url_for
from app.models.sql_alchemy import User
from app.status_codes import HTTP_CONFLICT_CODE


def register():
    if request.method == 'POST':
        name = request.form.get('username')
        email = request.form.get('email')
        if current_app.users_repository.query(email=email):
            return Response('User already exist', status=HTTP_CONFLICT_CODE)
        password = current_app.pass_encoder(
            request.form.get('password', '').encode()
        ).hexdigest()

        try:
            current_app.users_repository.add(User(name=name, email=email, password=password))
        except Exception as e:
            return Response('Unable to register the user', status=500)
        return make_response(redirect(url_for('login')))
    return render_template('register.html', email=request.cookies.get('email'))
