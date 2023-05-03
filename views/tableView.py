def getLine(valuesColumns = [], isHead = False, max_width = 20):
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