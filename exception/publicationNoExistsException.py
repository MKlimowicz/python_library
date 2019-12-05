class PublicationNoExistsException(Exception):
    def __init__(self, text):
        super().__init__(f"Publikacja o takim tytule {text} nie istnieje")