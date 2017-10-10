start_index = 0
end_index = 100
tries = 0

while True:
	tries+=1
	middle_index = start_index + (end_index-start_index) // 2
	print(middle_index,' - Exactly (E), too low (L) or too high (H)?')
	#print('Start: ',start_index,'; middle: ',middle_index,'; end: ',end_index)

	result = input()
	# L - computer's guess is too low
	# H - computer's guess is too high
	# E - exactly! break
	if result=='E':
		print('Hooray! Thanks ;) I guessed in ',tries,' tries')
		break
	elif result=='L':
		start_index=middle_index
	else:
		end_index=middle_index