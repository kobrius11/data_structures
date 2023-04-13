class Node:
	def __init__(self, value):
		self.value = value
		self.next_node = None
		self.prev_node = None

	def set_next_node(self, node):
		self.next_node = node

	def get_next_node(self):
		return self.next_node

	def set_prev_node(self, node):
		self.prev_node = node

	def get_prev_node(self):
		return self.prev_node

	def get_value(self):
		return self.value

	
