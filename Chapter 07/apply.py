def apply(x, f):
	for i in range(len(x)):
		x[i] = f(x[i])
        
def times(x):
	def inner(y):
		return x * y
	return inner

def minus(x):
	def inner(y):
		return y - x
	return inner

x = [4, 2, 7, 4]
apply(x, times(2))
print(x)
apply(x, minus(13))
print(x)

from operator import add, sub, mul, gt
def bind1st(op, x):
	def inner(y):
		return op(x, y)
	return inner

x = [4, 2, 7, 4]
apply(x, bind1st(mul, 2))
print(x)
