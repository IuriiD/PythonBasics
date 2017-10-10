def LetterChanges(str): 
    alfabet = {'a':'B','b':'C','c':'D','d':'E','e':'F',
    'f':'G','g':'H','h':'I','i':'J','j':'K','k':'L','l':'M',
    'm':'N','n':'O','o':'P','p':'Q','q':'R','r':'S','s':'T',
    't':'U','u':'V','v':'W','w':'X','x':'Y','y':'Z','z':'A'}

    vovels = {'a':'A','e':'E','i':'I','o':'O','u':'U','y':'Y'}

    for k,v in alfabet.items():
        str=str.replace(k,v)
        print(str)

    str=str.lower()
    print(str,'!')
    
    for k,v in vovels.items():
        str=str.replace(k,v)
        print(str)

    return str
    
# keep this function call here  
print(LetterChanges('Hello my dear baby'))