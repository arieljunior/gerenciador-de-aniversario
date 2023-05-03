from entities.personEntity import Person
import infra.personRepository as personRepository
import personView

def startMenu():
    opcao = ""
    while opcao != "3":
        print("\n1 - consultar pessoas\n2 - cadastrar pessoa\n3 - sair")
        opcao = input("Digite uma opção: ")
        match opcao:
            case '1':
                print("----CONSULTAR PESSOAS---\n")
                personView.showAllPersons()
            case '2':
                print("----CADASTRAR PESSOA---\n")
                personView.registerPerson()
            case '3':
                print("PROGRAMA ENCERRADO")
            case other:
                print("opção inválida")