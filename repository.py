from person import Person

def getAllPersons():
    persons = []
    with open("dados/pessoas.csv", "r", encoding='utf8') as file:
        lineCount = 0
        for line in file:
            if lineCount == 0:
                lineCount +=1
            else:
                arrayLines = line.strip().split(",")
                myPerson = Person(arrayLines[0], arrayLines[1], arrayLines[2])
                persons.append(myPerson)
    return persons