from flask import current_app, render_template, request


def ticket(board_id, ticket_id):
    if request.method == 'GET':
        return render_template(
            'ticket.html',
            ticket=current_app.tickets_repository.query(id=ticket_id)[0]
        )
