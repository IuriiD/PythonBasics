def to_camel_case(text):
    inputlist = [a for a in text.replace('_','-').split('-')]
    for i in range(1,len(inputlist)):
    	inputlist[i]=inputlist[i][:1].upper()+inputlist[i][1:]
    return ''.join(inputlist)

print(to_camel_case("the-stealth-warrior"))


#def to_camel_case(text):
#    return text[0] + ''.join([w[0].upper() + w[1:] for w in text.replace("_", "-").split("-")])[1:] if text else ''