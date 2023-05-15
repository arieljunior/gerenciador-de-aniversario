import controllers.table as tableController

class Person:
    def __init__(self, fullname, datebirth, email):
        self.fullname = fullname
        self.datebirth = datebirth
        self.email = email
    
    def __str__(_self):
        return f"NOME COMPLETO = {_self.fullname} DATA DE ANIVERSÁRIO = {_self.datebirth} EMAIL = {_self.email}"
    
    def getLineToCSV(_self):
        return "\n" + ",".join([_self.fullname, _self.datebirth, _self.email])
    
    @staticmethod
    def showViewTablePersons(persons):
        headerTable = tableController.getLine(["NOME COMPLETO", "DATA ANIVERSÁRIO", "EMAIL"], True)
        print(headerTable)
        for person in persons:
            line = tableController.getLine([person.fullname, person.datebirth, person.email])
            print(line)