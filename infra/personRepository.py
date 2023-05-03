from entities.person import Person

PATH_DATA_PERSONS = "data/pessoas.csv"

def getAllPersons():
    persons = []
    with open(PATH_DATA_PERSONS, "r", encoding='utf8') as file:
        lineCount = 0
        for line in file:
            if lineCount == 0:
                lineCount +=1
            else:
                arrayLines = line.strip().split(",")
                myPerson = Person(arrayLines[0], arrayLines[1], arrayLines[2])
                persons.append(myPerson)
    return persons

def savePerson(person):
    if len(person.fullname) > 0 and len(person.datebirth) > 0 and len(person.email) > 0:
        with open(PATH_DATA_PERSONS, 'a') as file:
            newLine = person.getLineToCSV()
            file.write(newLine)
        return {"success": True, "message": f"{person.fullname} foi salvo com sucesso"}
    else:
        return {"success": False, "message": "Todos os campos são obrigatórios!"}