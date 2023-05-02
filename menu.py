from person import Person
import repository

def getLineTable(valuesColumns = [], isHead = False, max_width = 20):
    if len(valuesColumns) == 0:
        return ""
    
    result = ""
    widthBorder = -1
    for columnName in valuesColumns:
        myColumn = f"| {columnName} "

        if len(myColumn) < max_width:
            diff = max_width - len(myColumn)
            myColumn += " " * diff
        elif len(myColumn) > max_width:
            myColumn = myColumn[:max_width]

        widthBorder += len(myColumn)
        result += myColumn

    result += "|"

    if isHead == False:
        return result

    borderTop = " " + ("_" * widthBorder)
    borderBottom = " " + ("¨" * widthBorder)

    result = f"{borderTop}\n{result}\n{borderBottom}"

    return result

opcao = ""
while opcao != "3":
    print("\n1 - consultar pessoas\n2 - cadastrar pessoa\n3 - sair")
    opcao = input("Digite uma opção: ")
    match opcao:
        case '1':
            print("----CONSULTAR PESSOAS---\n")
            
            persons = repository.getAllPersons();
            headerTable = getLineTable(Person.getColumnsName(), True)

            print(headerTable)
            for person in persons:
                line = getLineTable([person.fullname, person.datebirth, person.email])
                print(line)
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