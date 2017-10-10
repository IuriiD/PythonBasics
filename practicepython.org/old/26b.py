game = 	[[1, 2, 0], [2, 1, 0], [2, 1, 1]]
one = 	[[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]]
winner_is_2 = [[2, 2, 0], [2, 1, 0], [2, 1, 1]]
winner_is_1 = [[1, 2, 0], [2, 1, 0], [2, 1, 1]]
winner_is_also_1 = [[0, 1, 0], [2, 1, 0], [2, 1, 1]]
no_winner = [[1, 2, 0], [2, 1, 0], [2, 1, 2]]
also_no_winner = [[1, 2, 0], [2, 1, 0], [2, 1, 0]]

# takes list of lists and prints it's lists one by one
def horiz_check(game):
	work_arr = []
	for i in range(len(game)):
		work_arr = game[i] # here's our line
		if all(x==work_arr[0] for x in work_arr) and work_arr[0]!=0:
			return work_arr[0]

# takes list of lists (of equal length) and prints lists composed of 1st/2nd/3rd etc elements of every list
def vert_check(game):
	for i in range(len(game[0])):
		work_arr = []
		for x in range(len(game)):
			work_arr.append(game[x][i])
			#print(work_arr)
		if all(x==work_arr[0] for x in work_arr) and work_arr[0]!=0:
			return work_arr[0]

def diagon_check(game):
	if len(game)==len(game[0]):
		# diagonal 1
		work_arr = []
		for i in range(len(game)):
			work_arr.append(game[i][i])
		if all(x==work_arr[0] for x in work_arr) and work_arr[0]!=0:
			return work_arr[0]
		# diagonal 2
		work_arr = []
		for i in range(len(game)):
			work_arr.append(game[i][len(game[0])-1-i])
		if all(x==work_arr[0] for x in work_arr) and work_arr[0]!=0:
			return work_arr[0]
	else:
		print('Diagonals only in square fields (e.g. 3x3, 5x5 etc')
		return None

mylist = also_no_winner
if horiz_check(mylist)==1 or vert_check(mylist)==1 or diagon_check(mylist)==1:
	print('1!')
elif horiz_check(mylist)==2 or vert_check(mylist)==2 or diagon_check(mylist)==2:
	print('2!')
else:
	print('Tie!')