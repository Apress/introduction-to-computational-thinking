def fibrec(n):
    if n <= 1: return 1
    return fibrec(n - 1) + fibrec(n - 2)

tbl = {}
def fibtbl(n):
    if n <= 1: return 1
    if n not in tbl:
        tbl[n] = fibtbl(n - 1) + fibtbl(n - 2)
    return tbl[n]

from functools import cache
@cache
def fibcache(n):
    if n <= 1: return 1
    return fibcache(n - 1) + fibcache(n - 2)

def fibdp(n):
    if n <= 1:
        return 1
    fi1, fi2 = 1, 1
    for i in range(n - 1):
        fi1, fi2 = fi1 + fi2, fi1
    return fi1

for n in range(10):
    print(f"fibrec({n}) = {fibrec(n)}, fibtbl({n}) = {fibtbl(n)}, fibcache({n}) = {fibcache(n)}, fibdp({n}) = {fibdp(n)}")

