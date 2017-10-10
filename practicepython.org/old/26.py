game = 	[[1, 2, 0],
		[2, 1, 0],
		[2, 1, 1]]

winner_is_2 = [[2, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

winner_is_1 = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

winner_is_also_1 = [[0, 1, 0],
	[2, 1, 0],
	[2, 1, 1]]

no_winner = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 2]]

also_no_winner = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 0]]

def playerwins(n,l): # n - player number, 1 or 2, l - 3x3 array
	if [0][0]==n and l[0][1]==n and l[0][2]== n or \
	l[0][0]==n and l[1][1]==n and l[2][2]==n or\
	l[0][0]==n and l[1][0]==n and l[2][0]==n or\
	l[0][1]==n and l[1][1]==n and l[2][1]==n or\
	l[0][2]==n and l[1][1]==n and l[2][0]==n or\
	l[0][2]==n and l[1][2]==n and l[2][2]==n or\
	l[1][0]==n and l[1][1]==n and l[1][2]==n or\
	l[2][0]==n and l[2][1]==n and l[2][2]==n:
		return True
	else:
		return False

if playerwins(1,also_no_winner)==True:
	print('Player 1 wins!')
if playerwins(2,also_no_winner)==True:
	print('Player 2 wins!')
if playerwins(1,also_no_winner)==False and playerwins(2,also_no_winner)==False:
	print('Tie!')

# player 1 wins if:
'''
[0][0]+[0][1]+[0][2] or
[0][0]+[1][1]+[2][2] or
[0][0]+[1][0]+[2][0]
or
[0][1]+[1][1]+[2][1]
or 
[0][2]+[1][1]+[2][0] or
[0][2]+[1][2]+[2][2]
or
[1][0]+[1][1]+[1][2] 
or
[2][0]+[2][1]+[2][2]
'''
