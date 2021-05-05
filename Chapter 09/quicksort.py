
# dummy pivot picker...pics first element
pick_pivot = lambda x: x[0]

def qsort(xs):
    if len(xs) < 2: return xs
    p = pick_pivot(xs)

    first = qsort([x for x in xs if x < p])
    middle = [x for x in xs if x == p]
    last = qsort([x for x in xs if x > p])

    return first + middle + last

x = [1, 7, 2, 7, 8, 9, 3, 4]
print(qsort(x))

# Witout list-comprehension
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

def qsort_rec(x, i, j):
    if j - i <= 1: return
    k = partition(x, i, j)
    qsort_rec(x, i, k)
    qsort_rec(x, k + 1, j)

def qsort(x):
    qsort_rec(x, 0, len(x))
    return x # Only returning for ease of use

print(qsort(x))
