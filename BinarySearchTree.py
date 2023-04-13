from random import randint


class BinarySearchTree:
	def __init__(self, value, depth=1):
		self.value = value
		self.depth = depth
		self.left = None
		self.right = None


	def insert(self, value):
		if self.value > value:
#if self.left is not none (exists), recursively call insert on self.left till self.left is none.
			if self.left:
				self.left.insert(value)
#when self.left is None, make self.left a new bst class instance with depth + 1
			else:
				self.left = BinarySearchTree(value, self.depth + 1)
				print(f'Tree node {value} added to the left of {self.value} at depth {self.depth + 1}')
#if root value is less than value, do same thing with a self.right
		else:
			if self.right:
				self.right.insert(value)
			else:
				self.right = BinarySearchTree(value, self.depth + 1)
				print(f'Tree node {value} added to the right of {self.value} at depth {self.depth + 1}')


	def get_node_by_value(self, value):
#base case, if value exists
		if self.value == value:
			return self
#recursive step, if child exists and which child is traversed
		elif self.left and self.value > value:
			self.left.get_node_by_value(value)

		elif self.right and self.value < value:
			self.right.get_node_by_value(value)
		else:
			return None


	def depth_first_traversal(self):
		if self.left:
			return self.left.depth_first_traversal()
		print(f'Depth={self.depth}, Value={self.value}')
		if self.right:
			return self.right.depth_first_traversal()

#testing
#tree = BinarySearchTree(15)

#for x in range(10):
	#tree.insert(randint(0, 100))

#tree.depth_first_traversal()

print('py', print('py', print('py')))
