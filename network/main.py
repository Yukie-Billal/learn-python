class Cars():
	def __init__(self, name):
		self.name = name

	def speedUp(self):
		print(self.name," is speed up!")

def createCars(name):
	return Cars(name) 