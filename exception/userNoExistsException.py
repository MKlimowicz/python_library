class UserNoExistsException(Exception):
    def __init__(self, id):
        super().__init__(f'Uzytkownik o takim id: {id} nie istnieje')