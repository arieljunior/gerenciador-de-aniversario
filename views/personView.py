import infra.personRepository as personRepository
import tableView
import entities.personEntity as Person

def showAllPersons():
    persons = personRepository.getAllPersons();
    headerTable = tableView.getLine(Person.getColumnsName(), True)

    print(headerTable)
    for person in persons:
        line = tableView.getLine([person.fullname, person.datebirth, person.email])
        print(line)

def registerPerson():
    fullname = input("Digite o nome completo: ")
    datebirth = input("Digite a data de nascimento: ")
    email = input("Digite o e-mail: ")

    myPerson = Person(fullname, datebirth, email)
    result = personRepository.savePerson(myPerson)

    print(result.get("message", "Usuário salvo com sucesso!"))