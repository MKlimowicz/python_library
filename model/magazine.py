from model.book import Book
import datetime

from model.publication import Publication


class Magazine(Publication):
    def __init__(self, language, title, publisher, year):
        super().__init__(title=title, publisher=publisher, year=year)
        self._language = language
        self._monthDay = datetime.date(2016, 1, 16)

    def __str__(self):
        return f"tytuł: {self.getTitle()} jezyk: {self._language} data publikacji: {self._monthDay}"

    def getLanguage(self):
        return self._language

    def getDate(self):
        return self._monthDay


