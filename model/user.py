class User:
    def __init__(self, name, lastName, pesel):
        self._id = None
        self._name = name
        self._lastName = lastName
        self._pesel = pesel


    def __str__(self):
        return f"Id: {self._id} Imie: {self._name}, nazwisko: {self._lastName}, pesel: {self._pesel}"

    def getPesel(self):
        return self._pesel

    def getId(self):
        return self._id

    def setId(self, id):
        self._id = id

    def getName(self):
        return self._name

    def getLastName(self):
        return self._lastName