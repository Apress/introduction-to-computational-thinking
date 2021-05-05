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

import operator
add = curry(operator.add)
add2 = add(2)
x = [1, 2, 3]
apply(x, add2)
print(x)
