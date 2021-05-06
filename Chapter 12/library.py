class LibraryItem(object):
    def __init__(self, name):
        self.name = name

    def loan(self):
        print(f"Loaning {self.name}")

    def ret(self):
        print(f"Returning {self.name}")

class Book(LibraryItem):
    def read(self):
        print(f"Reading {self.name}")

class DVD(LibraryItem):
    def watch(self):
        print(f"Watching {self.name}")

book = Book("John Dies at the End")
book.loan() # The LibraryItem method
book.read()
book.ret()  # The LibraryItem method

dvd = DVD("The Princess Bride")
dvd.loan()  # The LibraryItem method
dvd.watch()
dvd.ret()   # The LibraryItem method


class Underwear(LibraryItem):
    def ret(self):
        super().ret()
        print("Please don't return used underwear")

un = Underwear("Pants")
un.loan()
un.ret()
