# apply and curry for testing...
def apply(x, f):
	for i in range(len(x)):
		x[i] = f(x[i])

from inspect import signature
def number_of_arguments(f):
	return len(signature(f).parameters)

def curry(f):
	no_args = number_of_arguments(f)
	def bind_args(args):
		def wrap(x):
			next_args = args + (x,)
			if len(next_args) == no_args:
				# we got the last arg
				return f(*next_args)
			else:
				return bind_args(next_args)
		return wrap
	return bind_args(args = ())



from operator import add, sub

def switch_params(op):
	def switch(x, y):
		return op(y, x)
	return switch


x = [1, 2, 3]
minus = curry(switch_params(sub))
apply(x, minus(13))
print(x)

def compose(f, g):
	def inner(x):
		return f(g(x))
	return inner

switch_curry = compose(curry, switch_params)
minus = switch_curry(sub)

x = [1, 2, 3]
apply(x, minus(13))
print(x)
