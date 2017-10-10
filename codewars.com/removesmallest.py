def remove_smallest(numbers):
    minimal = min(numbers)
    if minimal:
    	numbers.remove(minimal)
    return numbers

print(remove_smallest([2,2,1,2,1]))