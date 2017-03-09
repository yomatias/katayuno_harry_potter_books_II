class BookGroup:
	def __init__(self):
		self.title = ''
		self.quantity = 0

	def __str__(self):
		return "title: "+str(self.title)+" - quantity: "+str(self.quantity)
