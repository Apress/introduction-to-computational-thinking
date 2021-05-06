from datetime import datetime

class Log(object):
	def __init__(self):
		self.log = []

	def add_entry(self, entry):
		now = datetime.now()
		self.log.append("{}: {}".format(now, entry))

	def print_entries(self):
		for entry in self.log:
			print(entry)

log = Log()
log.add_entry("foo")
log.add_entry("bar")
log.add_entry("baz")
log.print_entries()
