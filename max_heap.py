class MaxHeaps:
	def __init__(self, value, index= 0):
		self.value = value
		self.left = None
		self.right = None
		self.index = index


	def add(self, value):
		if value < self.value:
			if self.left is None:
				self.left = MaxHeaps(value, (self.index *2) + 1)
			else:
				self.left.add(value)

		if value > self.value:
			if self.right is None:
				self.right =  MaxHeaps(value, (self.index *2) + 2)
			else:
				self.right.add(value)

	def listify(self):
		lst = []
		




