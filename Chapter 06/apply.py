def apply(x, f):
	for i in range(len(x)):
		x[i] = f(x[i])

def times_two(x):
	return 2 * x

def minus_13(x):
	return x - 13

x = [1, 2, 3]
apply(x, times_two)
print(x)
apply(x, minus_13)
print(x)
