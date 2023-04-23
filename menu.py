from person import Person
import repository

opcao = ""
while opcao != "3":
    print("\n1 - consultar pessoas\n2 - cadastrar pessoa\n3 - sair")
    opcao = input("Digite uma opção: ")
    match opcao:
        case '1':
            print("----CONSULTAR PESSOAS---\n")
            persons = repository.getAllPersons();
            for person in persons:
                print(person.toString())
        case '2':
            print("----CADASTRAR PESSOA---\n")

            fullname = input("Digite o nome completo: ")
            datebirth = input("Digite a data de nascimento: ")
            email = input("Digite o e-mail: ")

            myPerson = Person(fullname, datebirth, email)
            result = repository.savePerson(myPerson)
    
            print(result.get("message", "Usuário salvo com sucesso!"))


        case '3':
            print("PROGRAMA ENCERRADO")
        case other:
            print("opção inválida")