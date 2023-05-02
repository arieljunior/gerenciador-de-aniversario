class Person:
    def __init__(self, fullname, datebirth, email):
        self.fullname = fullname
        self.datebirth = datebirth
        self.email = email
    
    def __str__(_self):
        return f" NOME COMPLETO = {_self.fullname}\n DATA DE ANIVERSÁRIO = {_self.datebirth}\n EMAIL = {_self.email}\n"
    
    def getLineToCSV(_self):
        return "\n" + ",".join([_self.fullname, _self.datebirth, _self.email])
    
    @staticmethod
    def getColumnsName():
        return ["NOME COMPLETO", "DATA ANIVERSÁRIO", "EMAIL"]
    
# print(Person("ariel junior", "17/05/1996", "ariel@teste.com"))