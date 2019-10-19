from flask import current_app, render_template, request, redirect, url_for
from app.models.sql_alchemy import Ticket


def tickets(board_id):
    if request.method == 'GET':
        return render_template(
            'tickets.html',
            board_id=board_id,
            tickets=current_app.tickets_repository.query(dashboard_id=board_id)
        )
    elif request.method == 'POST':
        model = Ticket(
            **{
                'creator_id': request.user.id,
                'dashboard_id': board_id,
                **request.form
            }
        )
        current_app.tickets_repository.add(model)
        return redirect(url_for('tickets', board_id=board_id))
