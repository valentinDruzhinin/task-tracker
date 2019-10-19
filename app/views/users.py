from flask import current_app, render_template


def users(user_id):
    user_name = current_app.users_repository.query(id=user_id)[0].name
    return render_template('users.html', user_name=user_name, user_id=user_id)
