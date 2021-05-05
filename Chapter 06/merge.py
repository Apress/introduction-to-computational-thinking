def merge(x, y):
	result = []
	i, j = 0, 0
	while True:
		if i == len(x):
			# no more elements in x
			while j < len(y):
				result.append(y[j])
				j += 1
			return result
		if j == len(y):
			# no more elements in y
			while i < len(x):
				result.append(x[i])
				i += 1
			return result
		if x[i] < y[j]:
			result.append(x[i])
			i += 1
		else:
			result.append(y[j])
			j += 1
