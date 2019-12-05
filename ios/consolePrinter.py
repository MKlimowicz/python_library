from typing import List

from model.book import Book
from model.borrowHistory import BorrowHistory
from model.magazine import Magazine
from model.user import User


def printLine(text: str):
    print(text)


class ConsolePrinter:
    def __init__(self):
        pass

    def printBooks(self, publications):
        filterPublications = list(filter(lambda p: type(p) == Book, publications))
        if len(filterPublications) > 0:
            for publication in filterPublications:
                printLine(publication)
        else:
            printLine("---Niestety niema książek w bibliotece---")

    def printMagazine(self, publications):
        filterPublications = list(filter(lambda p: type(p) == Magazine, publications))
        if len(filterPublications) > 0:
            for publication in filterPublications:
                printLine(publication)
        else:
            printLine("---Niestety niema magazynów w bibliotece---")

    def printUsers(self, users: List[User]):
        for user in users:
            printLine(user)

    def printBorrowHistory(self, borrowHistory: BorrowHistory):
        for bh in borrowHistory:
            printLine(bh)

