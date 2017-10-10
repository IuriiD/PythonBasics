textinput = input('Please enter some phrase: ')

textsplit = textinput.split()
# reversedlist = textsplit[::-1]
result = ' '.join(textsplit[::-1])
print(result)