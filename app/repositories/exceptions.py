class DataBaseError(Exception):
    def __init__(self):
        super().__init__('Unable to connect to Database')
