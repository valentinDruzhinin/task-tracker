from flask import current_app, render_template

from app.queries import SQLQuery


def users(user_id):
    user_name = current_app.db.execute(SQLQuery.GET_USER_NAME_BY_ID, user_id).fetchone()[0]
    return render_template('users.html', user_name=user_name, user_id=user_id)
