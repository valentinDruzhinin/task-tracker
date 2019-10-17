from flask import render_template, request


def index():
    return render_template(
        'index.html', email=request.cookies.get('email')
    )
