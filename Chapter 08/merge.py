def merge_rec(x, y, i = 0, j = 0):
	if i == len(x):	return y[j:]
	if j == len(y):	return x[i:]
	if x[i] < y[j]:
		res = merge_rec(x, y, i + 1, j)
		res.append(x[i])
		return res
	else:
		res = merge_rec(x, y, i, j + 1)
		res.append(y[j])
		return res

def merge(x, y):
	return list(reversed(merge_rec(x, y)))

x = [1, 5, 7, 8]
y = [2, 3, 6, 9]
print(merge(x, y))


def app(lst, x):
	lst.append(x)
	return lst

def merge(x, y, i = 0, j = 0, acc = None):
	if acc is None: acc = []
	if i == len(x):	return acc + y[j:]
	if j == len(y):	return acc + x[i:]
	if x[i] < y[j]:
		return merge(x, y, i + 1, j, app(acc, x[i]))
	else:
		return merge(x, y, i, j + 1, app(acc, y[j]))
print(merge(x, y))
