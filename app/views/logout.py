from flask import make_response, url_for, redirect


def logout():
    resp = make_response(redirect(url_for('login')))
    resp.set_cookie('email', '')
    return resp
