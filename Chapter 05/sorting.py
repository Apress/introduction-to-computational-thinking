y = [1, 5, 2, 7, 3, 7, 2, 3, 9]

x = y[::] # make a copy to sort
x.sort()
print("Builtin sort:  ", x)

# Selection sort
x = y[::] # make a copy to sort
for i in range(len(x)):
	# find index of smallest elm in x[i:]
	min_idx, min_val = i, x[i]
	for j in range(i, len(x)):
		if x[j] < min_val:
			min_idx, min_val = j, x[j]
			
	# swap x[i] and x[j] puts
	# x[j] at the right position
	x[i], x[min_idx] = min_val, x[i]
print("Selection sort:", x)

# Insertion sort
x = y[::] # make a copy to sort
for i in range(1,len(x)):
	j = i
	while j > 0 and x[j-1] > x[j]:
		x[j-1], x[j] = x[j], x[j-1]
		j -= 1
print("Insertion sort:", x)

# Bubble sort
x = y[::] # make a copy to sort
while True:
	swapped = False
	for i in range(1,len(x)):
		if x[i-1] > x[i]:
			x[i-1], x[i] = x[i], x[i-1]
			swapped = True

	if not swapped:
		break
print("Bubble sort:   ", x)

# Cocktail sort
x = y[::] # make a copy to sort
while True:
	swapped = False
	for i in range(1, len(x)):
		if x[i-1] > x[i]:
			x[i-1], x[i] = x[i], x[i-1]
			swapped = True
				
	if not swapped:
		break

	for i in range(len(x)-1, 0, -1):
		if x[i-1] > x[i]:
			x[i-1], x[i] = x[i], x[i-1]
			swapped = True

	if not swapped:
		break
print("Cocktail sort: ", x)

# bucket sort
x = y[::]
m = max(x) + 1 # we need one more than the largest number as the number of buckets
buckets = [0] * m
for key in x:
	buckets[key] += 1
i = 0
for key in range(m):
	for j in range(buckets[key]):
		x[i] = key
		i += 1    
print("Bucket sort:   ", x)

# Radix sort -- this is silly since we have small numbers, but still...
keys = y[::]
m = 256 # the maximum number in a byte
n = len(keys)
d = 4 # we have four sub-keys per value
subkeys = [
        (k         & 0xff
        ,(k >> 8)  & 0xff
        ,(k >> 16) & 0xff
        ,(k >> 24) & 0xff)
    for k in keys]
for j in range(d):
	buckets = [[] for bucket in range(m)]
	for i in range(n):
		key = keys[i]
		subkey = subkeys[i][j]
		buckets[subkey].append(key)

	keys = []
	for subkey in range(m):
		for key in buckets[subkey]:
			keys.append(key)

print("Radix sort:    ", keys)
