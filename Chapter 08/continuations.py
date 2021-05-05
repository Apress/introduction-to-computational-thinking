def identity(x): return x

def sum_cont(x, cont = identity):
    if x == []:
        return cont(0)
    else:
        def new_cont(y):
            return cont(x[0] + y)
        return sum_cont(x[1:], new_cont)

x = [1, 2, 3]
print(sum_cont(x))

def fib(n, return_point = identity):
    if n == 0 or n == 1:
        return return_point(1)
    else:
        def first_point(x):
            def second_point(y):
                return return_point(x + y)
            return fib(n - 2, second_point)

        return fib(n - 1, first_point)

for i in range(6):
    print(f"fib({i}) = {fib(i)}")

def fib(n, cont = lambda x: x):
    if n == 0 or n == 1:
        return cont(1)
    else:
        def next_cont(x):
            return fib(n - 2, lambda y: cont(x + y))
        return fib(n - 1, next_cont)

for i in range(6):
    print(f"fib({i}) = {fib(i)}")

def fib(n, cont = lambda x: x):
    if n == 0 or n == 1:
        return cont(1)
    else:
        return fib(n - 1, lambda x: fib(n - 2, lambda y: cont(x + y)))

for i in range(6):
    print(f"fib({i}) = {fib(i)}")
