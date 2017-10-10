def display(arr):
	for i in range(len(game)):
		print(game[i])

def move2game(arr,uinput,sign):
	u1_list = uinput.split(',')
	row = int(u1_list[0])-1
	column = int(u1_list[1])-1
	if arr[row][column]==0:
		arr[row][column]=sign
		return True
	else:
		print('Sorry, that block already checked, choose another one')
		return False

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
		#print('Diagonals only in square fields (e.g. 3x3, 5x5 etc')
		return None

def check4winner(mylist):
		if horiz_check(mylist)=='x' or vert_check(mylist)=='x' or diagon_check(mylist)=='x':
			print('Player "x" won!')
			return True
		elif horiz_check(mylist)=='*' or vert_check(mylist)=='*' or diagon_check(mylist)=='*':
			print('Player "*" won!')
			return True
		else:
			return False	

game = [[0,0,0],[0,0,0],[0,0,0]]

print('Let\'s play Tic-Tac-Toe!')
display(game)

while not check4winner(game):
	user1 = input('Player 1, your move ("row,column"): ')
	if not move2game(game,user1,'x'):
		user1 = input('Player 1, your move ("row,column"): ')
	display(game)

	user2 = input('Player 2, your move ("row,column"): ')	
	if not move2game(game,user2,'*'):
		user2 = input('Player 2, your move ("row,column"): ')	
	display(game)

	combined = set()
	combined.update(game[0],game[1],game[2])
	if 0 in combined:
		continue
	else:
		check4winner(game)
		break