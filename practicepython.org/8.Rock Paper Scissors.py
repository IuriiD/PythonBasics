pl1, pl2 = '', ''

while pl1 not in ['r', 'p', 's']:
	pl1 = input('Player 1, what do you choose? (rock - r, paper - p, scissors - s): ')
while pl2 not in ['r', 'p', 's']:
	pl2 = input('\nPlayer 2, What do you choose? (rock - r, paper - p, scissors - s): ')

if pl1==pl2:
	print('Tie game!')
else:
	if pl1=='r':
		if pl2=='s':
			print('Player 1 wins!')
		else:
			print('Player 2 wins')
	elif pl1=='p':
		if pl2=='r':
			print('Player 1 wins!')
		else:
			print('Player 2 wins')
	elif pl1=='s':
		if pl2=='p':
			print('Player 1 wins!')
		else:
			print('Player 2 wins')