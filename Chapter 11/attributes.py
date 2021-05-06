class Meta(type):
    def __getattribute__(self, name):
        print("Your class", self, "is trying to get", name)
        return 13
        
class MyClass(object, metaclass = Meta):
    def __getattribute__(self, name):
        print(self, "wants", name)
        return 42

obj = MyClass()
print(obj.foo)
print(obj.bar)
print(MyClass.foo)


class Meta(type):
    def __getattribute__(self, name):
        print("Your class", self, "is trying to get", name)
        return 13
        
class MyClass(object, metaclass = Meta):
    foo = "bar"
    
obj = MyClass()
print(obj.foo)


class MyClass(object):
    foo = "bar"
    def __getattribute__(self, name):
        d = super().__getattribute__("__dict__")
        cls_d = super().__getattribute__("__class__").__dict__
        return d[name] if name in d else cls_d[name]
    
obj = MyClass()
print(obj.foo)


class MyClass(object):
    def m(self): pass

    def __getattribute__(self, name):
        d = super().__getattribute__("__class__").__dict__
        res = super().__getattribute__(name)
        return d[name], res
    
obj = MyClass()
print(obj.m)


class MyClass(object):
    foo = "foo"
    def __init__(self):
        self.bar = "bar"
    def __getattr__(self, name):
        print("You tried to get", name)

obj = MyClass()
obj.foo
obj.bar
obj.baz


class MyClass(object):
    def __init__(self):
        self.foo = 42

    def __getattr__(self, name):
        print("You tried to get", name)
        return "no such luck!"

    def __setattr__(self, name, value):
        print("You told me to set", name, "to", value,
              "(but got 'foo')")
        self.__dict__[name] = 'foo'


obj = MyClass()
print(obj.foo)
print(obj.bar)
obj.bar = 42
print(obj.bar)

