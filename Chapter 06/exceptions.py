def raises_error(x):
	if x < 0:
		raise Exception("Negative", x)
	if x > 0:
		raise Exception("Positive", x)
	return 42

def f(x):
	return raises_error(x)

def g(x):
	try:
		print(f(x))
	except Exception as e:
		if e.args[0] == "Negative":
			print("g:", e.args[0])
			return f(0)
		else:
			raise

try:
	print(g(-1))
	print(g(1))
except Exception as e:
	print("Outer", e.args[0])
