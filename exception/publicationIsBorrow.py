class PublicationIsBorrow(Exception):
    def __init__(self, title):
        super().__init__(f"Książka o tytule {title} jest aktualnie wypozyczona")