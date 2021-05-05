def binary_sum(x):
	if len(x) == 0: return 0
	if len(x) == 1: return x[0]

	# O(n) work
	y = []
	for i in range(1, len(x), 2):
		y.append(x[i - 1] + x[i])
	if i + 1 < len(x): # handle odd lengths
		y[0] += x[i + 1]
	
	return binary_sum(y) # recurse on n//2 size

x = [1, 2, 3, 4, 5]
print(sum(x), binary_sum(x))
