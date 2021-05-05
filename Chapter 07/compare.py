def insertion_sort(x, greater_than):
	for i in range(1,len(x)):
		j = i
		while j > 0 and greater_than(x[j-1], x[j]):
			x[j-1], x[j] = x[j], x[j-1]
			j -= 1
	return x

def compare_index(i):
	def compare(x, y):
		return x[i] > y[i]
	return compare

x = [
	(1, "mark"),
	(6, "luke"),
	(2, "matthew"),
	(5, "gandalf"),
	(7, "john")
]
print(insertion_sort(x, compare_index(0)))
print(insertion_sort(x, compare_index(1)))

