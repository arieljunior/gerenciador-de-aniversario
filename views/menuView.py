from entities.personEntity import Person
import infra.personRepository as personRepository
import views.personView as personView
from email_validator import validate_email, EmailSyntaxError
import services.gmail as gmail
from datetime import datetime 
def startMenu():
    inputUser = ""
    while inputUser != "4":
        print("""1 - consultar pessoas
2 - Cadastrar pessoa
3 - Enviar email aos aniversariantes
4 - sair""")
        inputUser = input("Digite uma opção: ")
        match inputUser:
            case '1':
                print("----CONSULTAR PESSOAS---\n")
                startSubmenuConsultPersons()
            case '2':
                print("----CADASTRAR PESSOA---\n")
                personView.registerPerson()
            case '3':
                print("----ENVIAR EMAIL---\n")
                persons = personRepository.getBirthdays()

                if len(persons) == 0:
                    print("Nenhuma pessoa faz aniversário hoje")
                    continue

                listToSend = []
                for person in persons:
                    try:
                        validate_email(person.email)
                        listToSend.append({
                            "email": person.email,
                            "name": person.fullname
                        })
                    except:
                        continue
                if len(listToSend) > 0:
                    countEmailsSended = gmail.sendEmailBirthday(listToSend)
                    print(f"Foram enviados {countEmailsSended} emails")
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
                personView.showAllPersons()
                break
            case "2":
                personView.showBirthdays()
                break
            case "3":
                month = int(input("Qual é o mês (1 a 12)? "))
                personView.showPersonsByMonth(month)
                break
            case "4":
                break
            case other:
                print("Opção inválida")