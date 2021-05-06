class Account(object):
	def __init__(self, initial_balance):
		self.balance = initial_balance

	def insert(self, amount):
		self.balance += amount

	def withdraw(self, amount):
		if self.balance - amount < 0:
			raise Exception("Insufficient funds")
		self.balance -= amount

	def __repr__(self):
		return "Account({})".format(self.balance)

account = Account(10)
account.insert(5)
account.withdraw(10)
print(account)

try:
    account.withdraw(10)
except Exception as e:
    print(e)
