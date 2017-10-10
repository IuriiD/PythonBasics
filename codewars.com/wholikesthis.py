def likes(mylist):
	howmany = len(mylist)
	if howmany<=0: 
		return 'no one likes this'
	elif howmany==1:
		return mylist[0]+' likes this'
	elif howmany==2:
		return mylist[0]+' and '+mylist[1]+' like this'
	elif howmany==3:
		return '%s, %s and %s like this' % (mylist[0],mylist[1],mylist[2])
	else:
		return mylist[0]+', '+mylist[1]+' and '+str(len(mylist)-2)+' others like this'

print(likes(['1','2','2']))