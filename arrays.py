def countEvens(list):
	even = 0
	for number in list:
		if (number % 2 == 0):
			even = even+1

	return even

print countEvens([2, 2, 2, 2, 2, 2, 2, 2]) # expect 8
print countEvens([2, 8, 7, 8, 1, 1]) # expect 3


def sum13(list): 
	sum = 0 
	for i in range(0, len(list)):
		if not (list[i] == 13):
			sum = list[i] + sum 
		if list[i] == 13:
			i = i + 2

	return sum

print sum13([1, 2, 2, 1]) # expect 6
print sum13([1, 1]) # expect 2
print sum13([1, 2, 2, 1, 13]) # expect 6