x = 'accggggga'
y = 'acggtg'

def edit_dist(x, y, i = None, j = None):
    if i is None: i = len(x)
    if j is None: j = len(y)
    if i == 0: return j
    if j == 0: return i
    return min(
        edit_dist(x, y, i - 1, j - 1) + (x[i - 1] != y[j - 1]),
        edit_dist(x, y, i, j - 1) + 1,
        edit_dist(x, y, i - 1, j) + 1,
    )

print(f"Recursive edit_dist({x},{y}) = {edit_dist(x, y)}")

# Memoisation as if we had used the decorator (explicitly using
# cache() works the same way).
from functools import cache
edit_dist = cache(edit_dist)

print(f"Cached edit_dist({x},{y}) = {edit_dist(x, y)}")

def edit_dist(x, y, i = None, j = None, tbl = None):
    if i is None:   i = len(x)
    if j is None:   j = len(y)
    if tbl is None: tbl = {}
        
    if i == 0:
        tbl[i,j] = j
    elif j == 0:
        tbl[i,j] = i
    else:
        tbl[i,j] = min(
            edit_dist(x, y, i - 1, j - 1, tbl) + 
                        (x[i - 1] != y[j - 1]),
            edit_dist(x, y, i, j - 1, tbl) + 1,
            edit_dist(x, y, i - 1, j, tbl) + 1,
        )
    return tbl[i,j]

print(f"Memoise edit_dist({x},{y}) = {edit_dist(x, y)}")

import numpy as np
def build_edit_table(x, y):
    n, m = len(x), len(y)
    D = np.zeros((n + 1, m + 1), dtype = int) # dtype = int makes it a table of integers

    # base cases
    for i in range(n + 1):
        D[i, 0] = i
    for j in range(m + 1):
        D[0, j] = j

    # recursion
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            D[i,j] = min(
                D[i - 1, j - 1] + (x[i - 1] != y[j - 1]),
                D[i, j - 1] + 1,
                D[i - 1, j] + 1
            )

    return D

def edit_dist(x, y):
    D = build_edit_table(x, y)
    n, m = len(x), len(y)
    return D[n, m]

print(f"Dynamic programming edit_dist({x},{y}) = {edit_dist(x, y)}")



def backtrack_(D, x, y, i, j, path):
    if i == 0:
        path.extend('D' * j)
        return
    if j == 0:
        path.extend('I' * i)
        return

    left = D[i, j - 1] + 1
    diag = D[i - 1, j - 1] + (x[i - 1] != y[j - 1])
    up = D[i - 1, j] + 1

    dist = left
    op = 'D'
    if diag < dist:
        op = 'X' if x[i - 1] != y[j - 1] else '='
        dist = diag
    if up < dist:
        op = 'I'

    if op == 'D':
        backtrack_(D, x, y, i, j - 1, path)
    if op in ('=','X'):
        backtrack_(D, x, y, i - 1, j - 1, path)
    if op == 'I':
        backtrack_(D, x, y, i - 1, j, path)
    path.append(op)

def backtrack(D, x, y):
    n, m = len(x), len(y)
    path = []
    backtrack_(D, x, y, n, m, path)
    return ''.join(path)

D = build_edit_table(x, y)
ops = backtrack(D, x, y)
print(ops)

# This code, not in the book, makes an alignment of the two sequences
# from the backtracked operations.
a, b = [], []
i, j = 0, 0
for op in ops:
    if op in ('=', 'X'):
        a.append(x[i]) ; i += 1
        b.append(y[j]) ; j += 1
    elif op == 'I':
        a.append(x[i]) ; i += 1
        b.append('-')
    elif op == 'D':
        a.append('-')
        b.append(y[j]) ; j += 1
    else:
        assert False, "Unknown operation"

print(''.join(a))
print(''.join(b))
