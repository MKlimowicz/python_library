import datetime


class BorrowHistory:
    def __init__(self, id, pesel, title, start=datetime.datetime.now().date()):
        self.end = None
        self.id = id
        self.start = start
        self.pesel = pesel
        self.title = title
        self.text = 'Książka nie zostałą jeszcze zwrócona'

    def __str__(self):
        return f"id: {self.id}, data wypożyczenia: {self.start}, " \
               f"data oddania: {self.text if self.end is None else self.end}, " \
               f"pesel: {self.pesel}, tytuł: {self.title}"

    def getTitle(self):
        return self.title

    def setEnd(self):
        self.end = datetime.datetime.now().date()

    def setEndWithFile(self, end):
        self.end = end