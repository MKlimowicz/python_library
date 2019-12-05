from typing import List
from model.book import Book
from model.borrowHistory import BorrowHistory
from model.magazine import Magazine
from model.user import User


class FileManager:
    users: List[User] = []
    books: List[Book] = []
    magazines: List[Magazine] = []
    borrowHistory: List[BorrowHistory] = []

    def __init__(self):
        pass


    def downloadAllUserForFile(self):
        with open('c:/baza/users.txt', encoding='utf-8') as users:
            for user in users:
                userList = user.splitlines()[0].split(' ')
                newUser = self.createUser(userList)
                self.users.append(newUser)
        users.close()

    def downloadAllBookForFile(self):
        with open('c:/baza/books.txt') as books:
            for book in books:
                bookList = book.splitlines()[0].split(' ')
                newBook = self.createBook(bookList)
                self.books.append(newBook)
        books.close()

    def downloadAllMagazinesForFile(self):
        with open('c:/baza/magazines.txt', encoding='utf-8') as magazines:
            for magazin in magazines:
                magazineList = magazin.splitlines()[0].split(' ')
                newMagazine = self.createMagazine(magazineList)
                self.magazines.append(newMagazine)
        magazines.close()

    def downloadAllBorrowPublicationForFile(self):
        with open('c:/baza/borrow.txt', encoding='utf-8') as borrows:
            for borrow in borrows:
                borrowList = borrow.splitlines()[0].split(' ')
                newBorrow = self.createBorrow(borrowList)
                self.borrowHistory.append(newBorrow)

    def saveBorrowHistory(self, borrows: List[BorrowHistory]):
        borrowsFile = open('c:/baza/borrow.txt', encoding='utf-8', mode='w')
        for borrow in borrows:
            borrowsFile.write(f"{borrow.id} {borrow.end} {borrow.start} {borrow.pesel} {borrow.title}\n")
        borrowsFile.close()

    def saveUsers(self, users: List[User]):
        usersFile = open('c:/baza/users.txt', encoding='utf-8', mode='w')
        for user in users:
            usersFile.write(f'{user.getId()} {user.getName()} {user.getLastName()} {user.getPesel()}\n')
        usersFile.close()

    def savePublication(self, publications):
        magazinesFile = open('c:/baza/magazines.txt', encoding='utf-8', mode='w')
        bookFile = open('c:/baza/books.txt', mode='w')
        for pub in publications:
            if type(pub) == Book:
                book = pub
                bookFile.write(f'{book.getTitle()} {book.getPages()} {book.getIsbn()} {book.getTitle()} {book.getPublisher()} {book.getYear()}\n')
            elif type(pub) == Magazine:
                magazine = pub
                magazinesFile.write(f'{magazine.getLanguage()} {magazine.getTitle()} {magazine.getPublisher()} {magazine.getYear()} {magazine.getDate()}\n')
        magazinesFile.close()
        bookFile.close()

    def getAllUsers(self):
        self.downloadAllUserForFile()
        return self.users

    def getAllBook(self):
        self.downloadAllBookForFile()
        return self.books

    def getAllMagazine(self):
        self.downloadAllMagazinesForFile()
        return self.magazines

    def getAllBorrowHistory(self):
        self.downloadAllBorrowPublicationForFile()
        return self.borrowHistory

    def createUser(self, userList):
        id = userList[0]
        if len(id) == 2:
            id = id[1]
        name = userList[1]
        lastName = userList[2]
        pesel = userList[3]
        user = User(name, lastName, pesel)
        user.setId(int(id))
        return user

    def createBook(self, bookList):
        author = bookList[0]
        pages = int(bookList[1])
        isbn = bookList[2]
        title = bookList[3]
        publisher = bookList[4]
        year = int(bookList[5])
        return Book(author, pages, isbn, title, publisher, year)

    def createMagazine(self, magazineList):
        language = magazineList[0]
        title = magazineList[1]
        publisher = magazineList[2]
        year = int(magazineList[3])
        return Magazine(language, title, publisher, year)

    def createBorrow(self, borrowList):
        id = int(borrowList[0])
        end = borrowList[1]
        start = borrowList[2]
        pesel = borrowList[3]
        title = borrowList[4]
        bh = BorrowHistory(id, pesel, title, start)
        bh.setEndWithFile(end)
        return bh


