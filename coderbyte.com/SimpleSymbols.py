def SimpleSymbols(str): 
    if str[0].isalpha():
        return 'false'
    letters = []
    for i in range(1,len(str)):
        if str[i].isalpha():
            letters.append(str[i-1:i+2])
    for n in letters:
        if n[0]!='+' or n[2]!='+':
            return 'false'
            break
    return 'true'

print(SimpleSymbols('f++d+'))