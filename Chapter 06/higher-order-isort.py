def insertion_sort(x, greater_than):
	for i in range(1,len(x)):
		j = i
		while j > 0 and greater_than(x[j-1], x[j]):
			x[j-1], x[j] = x[j], x[j-1]
			j -= 1
	return x

x = [1, 6, 2, 7, 8]

def greater(x, y):
	return x > y
print(insertion_sort(x, greater))

def smaller(x, y):
	return y > x
print(insertion_sort(x, smaller))

x = [
	(1, "mark"),
	(6, "luke"),
	(2, "matthew"),
	(5, "gandalf"),
	(7, "john")
]

def first_greater(x, y):
	return x[0] > y[0]
def second_greater(x, y):
	return x[1] > y[1]

print(insertion_sort(x, first_greater))
print(insertion_sort(x, second_greater))
