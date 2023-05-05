from entities.personEntity import Person
import infra.personRepository as personRepository
import views.personView as personView

def startMenu():
    inputUser = ""
    while inputUser != "3":
        print("\n1 - consultar pessoas\n2 - cadastrar pessoa\n3 - sair")
        inputUser = input("Digite uma opção: ")
        match inputUser:
            case '1':
                print("----CONSULTAR PESSOAS---")
                startSubmenuConsultPersons()
            case '2':
                print("----CADASTRAR PESSOA---\n")
                personView.registerPerson()
            case '3':
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