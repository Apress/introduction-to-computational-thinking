def decorator(f):
	def g():
		print("g before calling f")
		return f()
	g.__name__ = f.__name__
	return g

@decorator
def f():
    print("Inside f")
    return 42

@decorator
def h():
    print("Inside f")
    return 42

f()
h()

print("f's name:", f.__name__)
print("h's name:", h.__name__)


def logged(f):
	def inner(*args, **kwargs):
		print("calling", f.__name__)
		result = f(*args, **kwargs)
		print("returning from", f.__name__)
		return result
	inner.__name__ = f.__name__
	return inner

@logged
def f(x):
    print('called f with argument', x)

f(42)

@logged
def f(x, y):
	return x + y

print(f(2, 3))

print('verbose levels...')
def logged(verbose_level = 0):
	def outer(f):
		def inner(*args, **kwargs):
			if verbose_level > 0:
				print("calling", f.__name__)
			result = f(*args, **kwargs)
			if verbose_level > 1:
				print("returning from", f.__name__)
			return result
		inner.__name__ = f.__name__
		return inner
	return outer

@logged(verbose_level = 1)
def f(x, y):
	return x + y
f(42, 21)

@logged(verbose_level = 2)
def g(x, y):
	return x + y
g(42, 21)

