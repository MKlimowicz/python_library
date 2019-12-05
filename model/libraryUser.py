from typing import List

from exception.publicationIsBorrow import PublicationIsBorrow
from exception.publicationNoBorrow import PublicationNoBorrow
from exception.userAlreadyExistsException import UserAlreadyExistsException
from exception.userNoExistsException import UserNoExistsException
from ios.file.fileManager import FileManager
from model.borrowHistory import BorrowHistory
from model.user import User
from ios.generatorId import Generator




class LibraryUser:
    users: List[User] = []
    historyBorrows: List[BorrowHistory] = []

    def __init__(self, fileManager: FileManager):
        self.file = fileManager
        self.users = self.file.getAllUsers()
        self.historyBorrows = self.file.getAllBorrowHistory()

    def addUser(self, user: User):
        filterUsers = list(filter(lambda u: u.getPesel() == user.getPesel(), self.users))
        if len(filterUsers) > 0:
            raise UserAlreadyExistsException(user.getPesel())
        else:
            user.setId(Generator.generateID(self.users))
            self.users.append(user)
            self.file.saveUsers(self.users)

    def getUsers(self):
        return self.users

    def findUserById(self, id):
        usersf = list(filter(lambda u: u.getId() == id, self.users))
        if len(usersf) == 0:
            raise UserNoExistsException(id)
        return usersf[0]

    def borrowBook(self, borrow: BorrowHistory):
        self.historyBorrows.append(borrow)
        self.file.saveBorrowHistory(self.historyBorrows)

    def findBorrowPublicationByTitle(self, title):
        borrowPublicationList = list(filter(lambda h: h.getTitle() == title, self.historyBorrows))
        isBorrow = True if len(borrowPublicationList) > 0 else False
        if isBorrow:
            raise PublicationIsBorrow(title)

    def getBorrowHistory(self):
        return self.historyBorrows

    def checkIfTheBookIsBorrowByTitle(self, title):
        borrowPublicationList = list(filter(lambda h: h.getTitle() == title, self.historyBorrows))
        isBorrow = True if len(borrowPublicationList) > 0 else False
        if not isBorrow:
            raise PublicationNoBorrow(title)

    def returnBook(self, title):
        for b in self.historyBorrows:
            if b.getTitle() == title:
                b.setEnd()
        self.file.saveBorrowHistory(self.historyBorrows)

