import random

# let's generate a list of numbers and sort it
#a = sorted([random.randint(1,80) for i in range(11)])
a = [3, 16, 22, 23, 26, 32, 36, 41, 41, 53, 64]

# let's generate another number
#b = random.randint(1,100)
b = 23

# a function takes a number and a list, divides the list in half 
#[(even list) or round(1/2list) and all-round(1/2list)]
# and then returns the list of two in which the number can be

def find(list,number):
	start_index = 0
	end_index = len(list)-1

	while True:
		middle_index = (end_index - start_index) // 2
		print(middle_index)

		if middle_index<start_index or middle_index<0 or middle_index>end_index:
			return False

		middle_element = list[middle_index]

		if middle_element==number:
			return True
		elif middle_element<number:
			end_index=middle_index
		else:
			start_index=middle_index

print(a)
print(b)
print(find(a,b))