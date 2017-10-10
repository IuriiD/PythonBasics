def LetterCapitalize(str):
    parced = [x for x in str.split()]
    result = []
    for i in parced:
        result.append(i[0].upper()+i[1:])
    final = ''
    final = ' '.join(result)
    return final

print(LetterCapitalize('hello world'))