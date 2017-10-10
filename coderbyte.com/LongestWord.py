def LongestWord(sen): 
    parced = sen.split()
    alphaonly = []
    for i in parced:
        temp = ''
        for n in i:
            if n.isalpha():
                temp+=n
        alphaonly.append(temp)
    print(alphaonly)
    # code goes here 
    return max(alphaonly, key = len)    

# keep this function call here  
#print LongestWord(raw_input())
myinput = 'Argument goes here'

print(LongestWord(myinput))