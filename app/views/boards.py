from flask import current_app, render_template, request, url_for, redirect
from app.models.sql_alchemy import Dashboard


def boards():
    if request.method == 'GET':
        return render_template(
            'dashboards.html',
            boards=current_app.dashboard_repository.query(creator_id=request.user.id)
        )
    if request.method == 'POST':
        model = Dashboard(**{'creator_id': request.user.id, **request.form})
        current_app.dashboard_repository.add(model)
        return redirect(url_for('boards', user_id=request.user.id))
