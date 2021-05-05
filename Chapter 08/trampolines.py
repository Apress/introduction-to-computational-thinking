def identity(x):
	return x

def thunk(f, *args):
    def delayed():
        return f(*args)
    return delayed

def trampoline(f):
    while callable(f):
        f = f()
    return f

def factorial_rec(n, cont = identity):
    if n <= 1:
        return thunk(cont, 1)
    else:
        def new_cont(x):
            return thunk(cont, n * x)
        return thunk(factorial_rec, n - 1, new_cont)

def factorial(n):
    return trampoline(factorial_rec(n))

def fib_rec(n, cont = identity):
    if n == 0 or n == 1:
        return cont(1)
    else:
        def first_recursive_cont(x):
            def second_recursive_cont(y):
                return thunk(cont, x + y)
            return thunk(fib_rec, n - 2, second_recursive_cont)
        return thunk(fib_rec, n - 1, first_recursive_cont)

def fib(n):
    return trampoline(fib_rec(n))

for n in range(6):
    print(f"{n}! = {factorial(n)}, fib({n}) = {fib(n)}")
print()



# With lambda expressions:
def factorial_rec(n, cont = lambda x: x):
    if n <= 1:
        return lambda: cont(1)
    else:
        return lambda: factorial_rec(n - 1, lambda x: lambda: cont(n * x))

def factorial(n):
    return trampoline(factorial_rec(n))

def fib_rec(n, cont = lambda x: x):
    if n == 0 or n == 1:
        return lambda: cont(1)
    else:
        def new_cont(x):
            return lambda: fib_rec(n - 2, lambda y: lambda: cont(x + y))
        return lambda: fib_rec(n - 1, new_cont)

def fib(n):
    return trampoline(fib_rec(n))

for n in range(6):
    print(f"{n}! = {factorial(n)}, fib({n}) = {fib(n)}")
print()
