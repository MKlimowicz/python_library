from ios.consolePrinter import ConsolePrinter
from model.book import Book
from model.magazine import Magazine
from model.user import User


class DataReader:
    def __init__(self):
        self.printer = ConsolePrinter()

    def getValueNumber(self) -> int:
        return int(input('Podaj wartość: '))

    def reandAdCreateBook(self) -> Book:
        title = input("Podaj tytuł: ")
        author = input("Autor: ")
        publisher = input("Wydawnictwo: ")
        isbn = input("ISBN: ")
        relaseDate = int(input("Rok wydania: "))
        pages = int(input("Podaj liczbe stron: "))

        return Book(author, pages, isbn, title, publisher, relaseDate)

    def readAndCreateMagazine(self):
        title = input("Podaj tytuł: ")
        language = input("Język: ")
        publisher = input("Wydawnictwo: ")
        relaseDate = int(input("Rok wydania: "))

        return Magazine(language, title, publisher, relaseDate)

    def readAndCreatUser(self):
        name = input("Podaj imie: ")
        lastName = input("Podaj nazwisko: ")
        pesel = input("Podaj numer pesel: ")
        
        return User(name, lastName, pesel)




