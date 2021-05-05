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


# If you are wondering if we could make the trampoline part a decorator,
# the answer is yes, but there is one complication. That will change what
# the name of the recursion function refers to (we change the variable so it
# refers to the wrapped function when we do that). You still need to use the
# original function for the recursion. One way to achive this is to make the
# function itself a parameter that we can bind in the function calls. In the
# examples below, I have called it `rec`, and I make sure we pass it in the
# wrapped function for the decorator.

def trampoline(f):
    def wrapper(*args, **kwargs):
        kwargs['rec'] = f # make sure we have the recursive function
        jumper = f(*args, **kwargs)
        while callable(jumper):
            jumper = jumper()
        return jumper
    wrapper.__name__ = f.__name__
    return wrapper

@trampoline
def factorial(n, rec, cont = lambda x: x):
    if n <= 1: return lambda: cont(1)
    else: return lambda: rec(n - 1, rec, lambda x: lambda: cont(n * x))

@trampoline
def fib(n, rec, cont = lambda x: x):
    if n == 0 or n == 1:
        return lambda: cont(1)
    else:
        def new_cont(x):
            return lambda: rec(n - 2, rec, lambda y: lambda: cont(x + y))
        return lambda: rec(n - 1, rec, new_cont) 

for n in range(6):
    print(f"{n}! = {factorial(n)}, fib({n}) = {fib(n)}")
print()
