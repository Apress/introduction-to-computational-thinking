from datetime import datetime

class logged(object):
    def __init__(self, f):
        self.log = []
        self.f = f

    def __call__(self, *args, **kwargs):
        now = datetime.now()
        self.log.append(f"{now}: calling {self.f.__name__}")
        return self.f(*args, **kwargs)

    def __get__(self, obj, cls):
        if obj is None: # we accessed through the class
            return self.log

		# If we are here, obj is not None, so return
		# a bound method.
        def bound(*args, **kwargs):
            return self(obj, *args, **kwargs)
        return bound

class Foo(object):
    @logged
    def say_hi(self):
        print("hi")

x = Foo()
x.say_hi() # get and call the bound method
print(Foo.say_hi) # get the list of logged items
