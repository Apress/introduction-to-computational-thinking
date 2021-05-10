from stack import Stack

def partition(x, i, j):
    pivot = x[i]
    k, h = i + 1, j - 1
    while k <= h:
        if x[k] <= pivot:
            k += 1
        elif x[k] > pivot:
            x[k], x[h] = x[h], x[k]
            h -= 1
    x[i], x[k - 1] = x[k - 1], x[i]
    return k - 1

def qsort(x):
    stack = Stack()

    # qsort_rec(x, 0, len(x))
    stack.push((0, len(x)))

    while stack:
        # qsort_rec(i, j)
        i, j = stack.pop()

        if j - i <= 1:
            # leave loop body to go to the
            # next stack frame
            continue

        k = partition(x, i, j)
        # qsort_rec(x, i, k)
        stack.push((i, k))
        # qsort_rec(x, k + 1, j)
        stack.push((k + 1, j))

x = [1, 6, 2, 4, 7]
qsort(x)
print(x)
