def Jumble(result:list):
    output:str = ''
    for letters in result:
        for letter in letters:
            output += letter
        output += ','
    return output[:len(output)-2]

def Jumble(letters:str):
    Result = []
    BI = []
    for x in range(2):
        BI.append(letters[x])


    Result.append(BI.copy())
    BI.reverse()
    Result.append(BI)
    return FormatResult(Result)

?