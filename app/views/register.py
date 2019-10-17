from flask import request, current_app, Response, render_template, make_response, redirect, url_for

from app.queries import SQLQuery
from app.status_codes import HTTP_CONFLICT_CODE


def register():
    if request.method == 'POST':
        name = request.form.get('username')
        email = request.form.get('email')
        if current_app.db.execute(SQLQuery.HAS_USER, (email,)).fetchone():
            return Response('User already exist', status=HTTP_CONFLICT_CODE)
        password = current_app.pass_encoder(
            request.form.get('password', '').encode()
        ).hexdigest()

        try:
            with current_app.db.begin() as conn:
                conn.execute(SQLQuery.INSERT_USER, (name, email, password))
        except Exception as e:
            # use logging
            print(f'Error : {e}')
            return Response('Unable to register the user', status=500)
        return make_response(redirect(url_for('login')))
    return render_template('register.html', email=request.cookies.get('email'))
