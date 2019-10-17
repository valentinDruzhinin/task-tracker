class SQLQuery:
    ALL_TICKETS = 'SELECT * FROM Tickets'
    TICKETS_BY_ASSIGNEE = 'SELECT * FROM Tickets WHERE assignee=%s'
    TICKETS_BY_CREATOR = 'SELECT * FROM Tickets WHERE creator_id=%s'
    GET_USER_NAME_BY_ID = 'SELECT name FROM Users WHERE id=%s'
    GET_USER_BY_EMAIL = 'SELECT * FROM Users WHERE email=%s'
    GET_USER = 'SELECT * FROM Users WHERE email=%s and password=%s'
    HAS_USER = 'SELECT * FROM Users WHERE email=%s'
    INSERT_USER = 'INSERT INTO Users(name, email, "password") VALUES (%s, %s, %s)'
    DELETE_USER = 'DELETE FROM Users WHERE email=%s'
    INSERT_TICKET = 'INSERT INTO ' \
                    'Tickets(title, description, date_of_creation, creator_id, dashboard_id) ' \
                    'VALUES (:title, :description, CURRENT_TIMESTAMP, :creator_id, :dashboard_id)'
    DELETE_TICKET = 'DELETE FROM Tickets WHERE id=%s'
    UPDATE_TICKET = 'UPDATE Tickets SET ' \
                    'title = :title, ' \
                    'description = :description, ' \
                    'date_of_creation = :date_of_creation, ' \
                    'creator_id = :creator_id, ' \
                    'dashboard_id = :dashboard_id, ' \
                    'assignee = :assignee, ' \
                    'status = :status ' \
                    'WHERE id = :id'
    GET_TICKETS = 'SELECT * FROM Tickets WHERE ' \
                  'id=:id OR ' \
                  'title=:title OR ' \
                  'creator_id=:creator_id OR ' \
                  'dashboard_id=:dashboard_id OR ' \
                  'assignee=:assignee OR ' \
                  'status=:status'
    CREATE_DASHBOARD = 'INSERT INTO ' \
                       'Dashboards(name, description, date_of_creation, creator_id) ' \
                       'VALUES (:name, :description, CURRENT_TIMESTAMP, :creator_id)'
    DELETE_DASHBOARD = 'DELETE FROM Dashboards WHERE id=%s'
    UPDATE_DASHBOARD = 'UPDATE Dashboards SET ' \
                       'name = :name, ' \
                       'description = :description, ' \
                       'date_of_creation = :date_of_creation, ' \
                       'creator_id = :creator_id ' \
                       'WHERE id = :id'
    GET_DASHBOARDS = 'SELECT * FROM Dashboards WHERE ' \
                     'id=:id OR ' \
                     'name=:name OR ' \
                     'creator_id=:creator_id'
