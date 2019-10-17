from flask import current_app, render_template, request


def board(board_id):
    if request.method == 'GET':
        return render_template(
            'dashboard.html',
            board=current_app.dashboard_repository.query(id=board_id)[0]
        )
