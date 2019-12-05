from typing import List

from exception.publicationAlreadyExistsException import PublicationAlreadyExistsException
from exception.publicationNoExistsException import PublicationNoExistsException
from ios.file.fileManager import FileManager
from model.magazine import Magazine
from model.publication import Publication


class Library:
    publications = dict()
    value: int

    def __init__(self, fileManager: FileManager):
        self.fileManager = fileManager
        self.__addBookOrMagazinesFromFile(self.fileManager.getAllBook())
        self.__addBookOrMagazinesFromFile(self.fileManager.getAllMagazine())

    def addPublication(self, publication: Publication):
        pubList = list(self.publications.values())
        pubListFilter = list(filter(lambda p: p.getTitle() == publication.getTitle(), pubList))

        if len(pubListFilter) > 0:
            raise PublicationAlreadyExistsException(publication.getTitle())

        self.publications[publication.getTitle()] = publication
        self.fileManager.savePublication(list(self.publications.values()))

    def getPublications(self):
        return list(self.publications.values())

    def findPublicationByTitle(self, title_publication: str) -> Publication:
        publications = list(self.publications.values())
        publicationsFilter = list(filter(lambda b: b.getTitle().lower() == title_publication.lower(), publications))
        if len(publicationsFilter) == 0:
            raise PublicationNoExistsException(title_publication)
        else:
            return publicationsFilter[0]

    def removePublication(self, publication):
        newPublications = dict()
        for (key, value) in self.publications.items():
            if value != publication:
                newPublications[key] = value
        self.publications.clear()
        self.publications = newPublications

    def findPublicationByTitleContainingValue(self, value):
        self.value = value
        publications = list(self.publications.values())
        filterPublications = list(filter(self.__isOccursValue, publications))

        if len(filterPublications) == 0:
            raise PublicationNoExistsException(value)
        return filterPublications

    def __isOccursValue(self, publication):
        if self.value in publication.getTitle().lower():
            return True
        return False

    def __addBookOrMagazinesFromFile(self, publications):
        for pub in publications:
            self.addPublication(pub)





