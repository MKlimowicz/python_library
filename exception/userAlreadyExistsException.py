class UserAlreadyExistsException(Exception):
    def __init__(self, pesel):
        super().__init__(f"Uzytkownik o takim numerze pesel {pesel} istnieje")