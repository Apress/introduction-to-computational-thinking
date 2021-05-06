class NegativeError(Exception):
	pass

class PositiveError(Exception):
	pass

def raises_error(x):
	if x < 0:
		raise NegativeError()
	if x > 0:
		raise PositiveError()
	return 42

def g(x):
	try:
		return raises_error(x)
	except NegativeError:
		print("g: Negative")
		return raises_error(0)

try:
	print(g(-1))
	print(g(1))
except Exception as e:
	print("Outer")


class ErrorOne(Exception):
	pass

class ErrorTwo(Exception):
	pass

class ErrorThree(Exception):
	pass

errors = [ErrorOne, ErrorTwo, ErrorThree]
for error in errors:
	try:
		raise error()
	except ErrorOne:
		print("ErrorOne")
	except ErrorTwo:
		print("ErrorTwo")
	except ErrorThree:
		print("ErrorThree")
