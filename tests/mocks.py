from mock import Mock


def create_db_mock():
    mock_db = Mock()
    mock_db._con = Mock()
    mock_db._con.execute = Mock()

    class ConManager:
        def __enter__(self):
            return mock_db._con

        def __exit__(self, exc_type, exc_val, exc_tb): ...

    mock_db.begin = ConManager
    return mock_db
