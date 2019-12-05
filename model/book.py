from model.publication import Publication


class Book(Publication):
    def __init__(self, author, pages, isbn, title, publisher, year):
        super().__init__(title=title, publisher=publisher, year=year)
        self._author = author
        self._pages = pages
        self._isbn = isbn

    def __str__(self):
        return f"author: {self._author}, tytuł: {self.getTitle()}, numer isbn: {self._isbn}"

    def getAuthor(self):
        return self._author

    def getPages(self):
        return self._pages

    def getIsbn(self):
        return self._isbn

