import enum

from exception.publicationAlreadyExistsException import PublicationAlreadyExistsException
from exception.publicationIsBorrow import PublicationIsBorrow
from exception.publicationNoBorrow import PublicationNoBorrow
from exception.publicationNoExistsException import PublicationNoExistsException
from exception.userAlreadyExistsException import UserAlreadyExistsException
from exception.userNoExistsException import UserNoExistsException
from ios.consolePrinter import ConsolePrinter, printLine
from ios.dataReader import DataReader
from ios.file.fileManager import FileManager
from model.borrowHistory import BorrowHistory
from model.library import Library
from model.libraryUser import LibraryUser
from ios.generatorId import Generator


class LibraryControl:
    def __init__(self):
        self.printer = ConsolePrinter()
        self.dataReader = DataReader()
        self.fileManager = FileManager()
        self.library = Library(self.fileManager)
        self.libraryUser = LibraryUser(self.fileManager)

    def controlLoop(self):
        while True:
            option: Option
            self.printOptions()
            option = self.getOption()
            if option == Option.EXIT:
                self.exit()
                break
            elif option == Option.ADD_BOOK:
                self.addBook()
                continue
            elif option == Option.PRINT_BOOK:
                self.printBook()
                continue
            elif option == Option.ADD_MAGAZINE:
                self.addMagazine()
                continue
            elif option == Option.PRINT_MAGAZINE:
                self.printMagazine()
                continue
            elif option == Option.DELETE_PUBLICATON:
                self.deletePublication()
                continue
            elif option == Option.FIND_PUBLICATON:
                self.findPublication()
                continue
            elif option == Option.ADD_USER:
                self.addUser()
                continue
            elif option == Option.PRINT_USER:
                self.printUser()
                continue
            elif option == Option.BORROW_PUBLICATION:
                self.borrowPublication()
                continue
            elif option == Option.PRINT_BORROW:
                self.printBorrowBook()
                continue
            elif option == Option.RETURN_BOOK:
                self.returnBorrowBook()
                continue

    def printOptions(self):
        printLine("Wybierz opcje: ")
        for option in Option:
            printLine(Option.toString(option.value))

    def getOption(self):
        optionOk = True
        option: Option
        while optionOk:
            try:
                option = Option.getOptionById(self.dataReader.getValueNumber())
                optionOk = False
            except ValueError:
                printLine("Wprowadzono wartość, która nie jest liczbą, podaj ponownie:")
            except UnboundLocalError:
                print('Brak opcji o takim id')
        return option

    def exit(self):
        printLine("Koniec programu żegnam")

    def addBook(self):
        try:
            book = self.dataReader.reandAdCreateBook()
            self.library.addPublication(book)
        except PublicationAlreadyExistsException as p:
            printLine(p.args)

    def printBook(self):
        self.printer.printBooks(self.library.getPublications())

    def addMagazine(self):
        try:
            magazine = self.dataReader.readAndCreateMagazine()
            self.library.addPublication(magazine)
        except PublicationAlreadyExistsException as p:
            printLine(p.args)

    def printMagazine(self):
        self.printer.printMagazine(self.library.getPublications())

    def deletePublication(self):
        try:
            title_publication = self.getTitlePublication()
            findPub = self.library.findPublicationByTitle(title_publication)
            self.library.removePublication(findPub)
        except PublicationNoExistsException as p:
            print(p.args)

    def getTitlePublication(self):
        printLine("Podaj tytuł publikacji która chcesz usunać")
        self.printBook()
        self.printMagazine()
        title_publication = input("Tytuł publikacji")
        return title_publication

    def findPublication(self):
        try:
            title_publication = input('Podaj tytuł, mogą byc pojedyncze znaki: ')
            findPub = self.library.findPublicationByTitleContainingValue(title_publication.lower())
            self.printer.printBooks(findPub)
            self.printer.printMagazine(findPub)
        except PublicationNoExistsException as p:
            print(p.args)

    def addUser(self):
        try:
            user = self.dataReader.readAndCreatUser()
            self.libraryUser.addUser(user)
        except UserAlreadyExistsException as u:
            printLine(u.args)

    def printUser(self):
        users = self.libraryUser.getUsers()
        self.printer.printUsers(users)

    def borrowPublication(self):
        try:
            title = self.__chooseBookToBorrow()
            self.library.findPublicationByTitle(title)
            self.libraryUser.findBorrowPublicationByTitle(title)

            idUser = self.__chooseTheUserWhoBorrow()
            user = self.libraryUser.findUserById(idUser)
            idBH = Generator.generateID(self.libraryUser.getBorrowHistory())
            borrowPublication = BorrowHistory(idBH, user.getPesel(), title)
            self.libraryUser.borrowBook(borrowPublication)

        except PublicationNoExistsException as p:
            printLine(p.args)
        except PublicationIsBorrow as b:
            printLine(b.args)
        except UserNoExistsException as u:
            printLine(u.args)

    def __chooseBookToBorrow(self):
        printLine('Podaj tytuł książki którą chcesz wypozyczyć: ')
        self.printMagazine()
        self.printBook()
        title = input('Tytuł')
        return title

    def __chooseTheUserWhoBorrow(self):
        printLine('Podaj id osoby która wypożycza książke: ')
        self.printUser()
        idUser = int(input('Podaj id: '))
        return idUser

    def printBorrowBook(self):
        self.printer.printBorrowHistory(self.libraryUser.getBorrowHistory())

    def returnBorrowBook(self):
        printLine('Podaj tytuł publikacji którą chcesz zwrócić: ')
        self.printBorrowBook()
        title = input('Podaj tytuł: ')

        try:
            self.libraryUser.checkIfTheBookIsBorrowByTitle(title)
            self.libraryUser.returnBook(title)
        except PublicationNoBorrow as p:
            printLine(p.args)


class Option(enum.Enum):
    EXIT = {0: "Wyjeście z programu"}
    ADD_BOOK = {1: "Dodanie książki"}
    ADD_MAGAZINE = {2: "Dodanie magazynu/gazety"}
    PRINT_BOOK = {3: "Wyświetl dostępne książki"}
    PRINT_MAGAZINE = {4: "Wyświetl dostępne magazyny"}
    DELETE_PUBLICATON = {5: "Usuń publikacje"}
    FIND_PUBLICATON = {6: "Znajdź publikacje"}
    ADD_USER = {7: "Dodaj użytkownika"}
    PRINT_USER = {8: "Wyswietl użytkownikow"}
    BORROW_PUBLICATION = {9: "Wypożycz książke"}
    PRINT_BORROW = {10: "Wyświetl wypozyczone książki"}
    RETURN_BOOK = {11: "Zwróć książkę"}


    def toString(option: dict) -> str:
        return "numer: {} czynność: {}".format(list(option.keys())[0]
                                            , list(option.values())[0])

    def getOptionById(id: int):
        optionR: Option
        for option in Option:
            if list(option.value.keys())[0] == id:
                optionR = option
        return optionR
