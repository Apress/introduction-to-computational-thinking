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

def merge_sort(x):
	if len(x) <= 1: return x
	mid = len(x) // 2
	return merge(merge_sort(x[:mid]), merge_sort(x[mid:]))


x = [1, 7, 2, 7, 8, 9, 3, 4]
print(merge_sort(x))

def merge_sort_rec(x, low, high):
	if high - low <= 1: return x[low:high]
	mid = (low + high) // 2
	return merge(merge_sort_rec(x, low, mid), 
		         merge_sort_rec(x, mid, high))

def merge_sort(x):
	return merge_sort_rec(x, 0, len(x))

x = [1, 7, 2, 7, 8, 9, 3, 4]
print(merge_sort(x))
