from flask import redirect, url_for, current_app, request, make_response
from itsdangerous import BadSignature


def auth():
    if request.path not in ['/login', '/register']:
        email = request.cookies.get('email', '')
        try:
            email = current_app.signer.unsign(email).decode()
            request.user = current_app.users_repository.query(email=email)[0]
            # add user into request
        except BadSignature:
            resp = make_response(redirect(url_for('login')))
            resp.set_cookie('email', '')
            return resp
