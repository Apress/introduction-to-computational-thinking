def split_sum(x, i, j):
    if i >= j:     return 0
    if i + 1 == j: return x[i]
    mid = (i + j) // 2
    return split_sum(x, i, mid) + split_sum(x, mid, j)

x = [1, 2, 3, 4, 5, 6]
print(sum(x), split_sum(x, 0, len(x)))

