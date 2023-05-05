import infra.personRepository as personRepository
import views.tableView as tableView
from entities.personEntity import Person
from datetime import date

def showTablePersons(persons):
    headerTable = tableView.getLine(Person.getColumnsName(), True)

    print(headerTable)
    for person in persons:
        line = tableView.getLine([person.fullname, person.datebirth, person.email])
        print(line)

def showAllPersons():
    persons = personRepository.getAllPersons();
    showTablePersons(persons)

def registerPerson():
    fullname = input("Digite o nome completo: ")
    datebirth = input("Digite a data de nascimento: ")
    email = input("Digite o e-mail: ")

    myPerson = Person(fullname, datebirth, email)
    result = personRepository.savePerson(myPerson)

    print(result.get("message", "Usuário salvo com sucesso!"))

def showPersonsByMonth(month: int):  
    if month < 1 or month > 12:
        print("Mês inválido")
        return
    persons = personRepository.getPersonsByMonth(month)
    if len(persons) == 0:
        print("Ninguém faz aniversário nesse mês")
        return
    showTablePersons(persons)

def showBirthdays():
    persons = personRepository.getBirthdays()
    if len(persons) == 0:
        print("Ninguém faz aniversário hoje")
        return
    
    showTablePersons(persons)
