def insertion_sort(x):
	for i in range(1,len(x)):
		j = i
		while j > 0 and x[j-1] > x[j]:
			x[j-1], x[j] = x[j], x[j-1]
			j -= 1
	return x
