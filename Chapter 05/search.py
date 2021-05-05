numbers = [1, 3, 5, 6, 7, 9]

# Linear search
x = 6
found = False
for n in numbers:
	if x == n:
		found = True
		break
print(found)

x = 2
found = False
for n in numbers:
	if x == n:
		found = True
		break
print(found)

# Binary search
x = 6
low, high = 0, len(numbers)
found = False
while low < high:
	mid = (low + high) // 2
	if numbers[mid] == x:
		found = mid
		break
	elif numbers[mid] < x:
		low = mid + 1
	else:
		high = mid
print(found)

x = 2
low, high = 0, len(numbers)
found = False
while low < high:
	mid = (low + high) // 2
	if numbers[mid] == x:
		found = mid
		break
	elif numbers[mid] < x:
		low = mid + 1
	else:
		high = mid
print(found)
