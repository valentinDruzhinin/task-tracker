from flask import redirect, url_for, current_app, request, make_response
from itsdangerous import BadSignature

from app.queries import SQLQuery


def auth():
    if request.path not in ['/login', '/register']:
        email = request.cookies.get('email', '')
        try:
            email = current_app.signer.unsign(email).decode()
            request.user = current_app.db.execute(SQLQuery.GET_USER_BY_EMAIL, email).fetchone()
            # add user into request
        except BadSignature:
            resp = make_response(redirect(url_for('login')))
            resp.set_cookie('email', '')
            return resp
