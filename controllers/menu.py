from models.person import Person
import infra.personRepository as personRepository
import services.email as email

def startMainMenu():
    inputUser = ""
    while inputUser != "4":
        print("\n1 - Consultar pessoas\n2 - Cadastrar nova pessoa\n3 - Enviar email aos aniversariantes\n4 - Sair")
        inputUser = input("Digite uma opção: ")
        match inputUser:
            case '1':
                print("----CONSULTAR PESSOAS---\n")
                startSubmenuConsultPersons()
            case '2':
                print("----CADASTRAR PESSOA---\n")
                registerPerson()
            case '3':
                print("----ENVIAR EMAIL PARA OS ANIVERSARIANTES---\n")
                sendEmailToBirthdays()
            case '4':
                print("PROGRAMA ENCERRADO")
            case other:
                print("opção inválida")

def startSubmenuConsultPersons():
    inputUser = ""
    
    print("""Consultar por: 
    1 - Todos
    2 - Aniversariantes
    3 - Aniversariantes de um mês específico
    4 - Voltar""")

    while inputUser != "4":
        inputUser = input("Digite uma opção: ")

        match inputUser:
            case "1":
                showAllPersons()
                break
            case "2":
                showBirthdays()
                break
            case "3":
                showPersonsByMonth()
                break
            case "4":
                break
            case other:
                print("Opção inválida")

def registerPerson():
    fullname = input("Digite o nome completo: ")
    datebirth = input("Digite a data de nascimento: ")
    email = input("Digite o e-mail: ")

    newPerson = Person(fullname, datebirth, email)
    result = personRepository.savePerson(newPerson)

    print(result.get("message", "Usuário salvo com sucesso!"))

def sendEmailToBirthdays():
    persons = personRepository.getBirthdays()

    if len(persons) == 0:
        print("Nenhuma pessoa faz aniversário hoje")
        return

    resp = input(f"{len(persons)} email(s) de aniversário para ser(em) enviado(s), deseja enviar ou ver os destinatários? (enviar/ver): ")
    
    if resp == "enviar":
        listToSend = [person for person in persons if email.isValidEmail(person.email)]
        countEmailsSended = email.sendEmailBirthday(listToSend)

        if countEmailsSended > 0:
            print(f"{countEmailsSended} email(s) enviado(s)")
        else:
            print("Não foi possível enviar email")
    elif resp == "ver":
        Person.showViewTablePersons(persons)
    else:
        print("Resposta inválida")

def showAllPersons():
    persons = personRepository.getAllPersons();
    Person.showViewTablePersons(persons)

def showBirthdays():
    persons = personRepository.getBirthdays()
    if len(persons) == 0:
        print("Ninguém faz aniversário hoje")
        return
    
    Person.showViewTablePersons(persons)

def showPersonsByMonth():  
    month = int(input("Qual é o mês (1 a 12)? "))
    if month < 1 or month > 12:
        print("Mês inválido")
        return
    persons = personRepository.getPersonsByMonth(month)
    if len(persons) == 0:
        print("Ninguém faz aniversário nesse mês")
        return
    Person.showViewTablePersons(persons)
