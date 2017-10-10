def tickets(people):
    if people[0]!=25:
    	return 'NO'
    else:
    	bills = [1,0] # N of $25 bills and N of $50 bills
    	for n in range(1,len(people)):
    		if people[n]==25:
    			bills[0]+=1
    		elif people[n]==50:
    			bills[0]-=1
    			if bills[0]<0:
    				return 'NO'
    		else:
    			if bills[1]>0:
    				bills[1]-=1
    				bills[0]-=1
    				if bills[0]<0:
    					return 'NO'
    			else:
    				bills[0]-=3
    				if bills[0]<0:
    					return 'NO'
    return 'YES'

print(tickets([25, 25, 25, 25, 50, 100, 50]))