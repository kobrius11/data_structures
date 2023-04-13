#FIFO, first in first out

from Node import Node


class Stack:
	def __init__(self):
		self.head_node = None

#return value methods
	#returns value, removing head
	def pop(self):
		node_to_remove = self.head_node
		self.head_node = node_to_remove.get_next_node()
		return node_to_remove.get_value()

	#returns value without removing head
	def peek(self):
		return self.head_node.get_value()

#add traverse methods
	def add_node(self, node):
		next_node = self.head_node
		node.set_next_node(next_node)
		self.head_node = node


	def traverse(self):
		current_node = self.head_node
		idx = 0

		while current_node:
			print(current_node.get_value())
			current_node = current_node.get_next_node()
			idx = idx + 1
		return


#represantation methods




