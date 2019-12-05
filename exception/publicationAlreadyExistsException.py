class PublicationAlreadyExistsException(Exception):
    def __init__(self, title):
        super().__init__(f"Publikacja o takim tytule {title} istnieje")
