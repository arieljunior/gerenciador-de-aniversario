class Person:
    def __init__(self, fullname, datebirth, email):
        self.fullname = fullname
        self.datebirth = datebirth
        self.email = email
    
    def toString(_self):
        return f"NOME COMPLETO = {_self.fullname}\nDATA DE ANIVERSÁRIO = {_self.datebirth}\nEMAIL = {_self.email}\n"