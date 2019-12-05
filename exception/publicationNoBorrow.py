class PublicationNoBorrow(Exception):
    def __init__(self, text):
        super().__init__(f"Ksiażka o takim tytule: {text} nie została wypozyczona")