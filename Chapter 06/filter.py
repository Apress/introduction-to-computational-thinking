def filter(x, p):
	y = []
	for elm in x:
		if p(elm):
			y.append(elm)
	return y

def is_even(x):
	return x % 2 == 0

x = [1, 2, 3, 4]
print(filter(x, is_even))
