def counter(i = 0):
    def thunk():
        return counter(i + 1)
    return i, thunk

i, next_count = counter()
for _ in range(5):
    print(i)
    i, next_count = next_count()
