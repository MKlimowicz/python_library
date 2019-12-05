class Publication:
    def __init__(self, title: str, publisher: str, year):
        self._title = title
        self._publisher = publisher
        self._year = year

    def getTitle(self):
        return self._title

    def getPublisher(self):
        return self._publisher

    def getYear(self):
        return self._year
