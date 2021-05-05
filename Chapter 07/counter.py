def counter():
	x = [0]
	def tick():
		x[0] += 1
		return x[0]
	return tick

c1 = counter()
c2 = counter()
print([c1(), c2(), c1(), c1(), c2()])

def counter():
	x = [0]
	def tick():
		x[0] += 1
	def val():
		return x[0]
	return tick, val

tick, val = counter()
tick()
print(val())
print(val())
tick()
tick()
print(val())
