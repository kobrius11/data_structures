from Node import Node

class LinkedList:
	def __init__(self):
		self.head_node = None
		self.tail_node = None

#set methods
	def set_head_node(self, node):
		next_node = self.head_node
		self.head_node = node
		self.head_node.set_next_node(next_node)


		current_node = self.head_node
		idx = 0

		while current_node:
			if current_node.get_next_node() == None:
				self.tail_node = current_node
			current_node = current_node.get_next_node()
			idx = idx + 1
			return

		


	def set_tail_node(self, node):

		prev_node = self.tail_node
		prev_node.set_next_node(node)
		self.tail_node = node
		self.tail_node.set_prev_node(prev_node)

	
#delete methods
	def delete_head_node(self):
		next_node = self.head_node.get_next_node()
		self.head_node = next_node


	def delete_tail_node(self):
		prev_node = self.tail_node.get_prev_node()
		self.tail_node = prev_node
		self.tail_node.set_next_node(None)


	def delete_by_value(self, value):
		current_node = self.head_node
		idx = 0

		while current_node:
			if current_node.get_value() == value:
				if current_node == self.head_node:
					return self.delete_head_node

				elif current_node == self.tail_node:
					return self.delete_tail_node

				next_node = current_node.get_next_node()
				prev_node = current_node.get_prev_node()

				prev_node.set_next_node(next_node)
				next_node.set_prev_node(prev_node)
				return
			current_node = current_node.get_next_node()
			idx = idx + 1


	#deletes node by index
	def delete_node(self, idx):
		current_node = self.head_node
		count = 0

		while current_node:
			if idx == count:
				if current_node == self.tail_node or idx == -1:
					return self.delete_tail_node

				elif current_node == self.head_node:
					return self.delete_head_node

				elif current_node == None:
					return None


				next_node = current_node.get_next_node()
				prev_node = current_node.get_prev_node()

				prev_node.set_next_node(next_node)
				next_node.set_prev_node(prev_node)
				
			current_node = current_node.get_next_node()
			count = count + 1

#add methods
	#adds node either to head or to tail or to index
	def add_node(self, node, add_to=0):
		idx = 0
		if self.head_node == None and self.tail_node == None:
			self.set_head_node(node)
			self.set_tail_node(node)
			return print(f"{node.get_value()} added to index: {idx}")

		elif add_to == -1:
			return self.set_tail_node(node)

		elif add_to == 0:
			return self.set_head_node(node)

		else:
			current_node = self.head_node
			

			while current_node:
				if idx == add_to:
					if current_node == self.tail_node:
						return self.set_tail_node(node)	
					next_node = current_node
					prev_node = current_node.get_prev_node()


					prev_node.set_next_node(node)
					next_node.set_prev_node(node)
					node.set_next_node(next_node)
					node.set_prev_node(prev_node)

					
					return f"Node added to index: {idx}"


				current_node = current_node.get_next_node()
				idx = idx + 1
				if add_to > idx:
					return 'add_node error: no such index'

				if add_to < idx:
					return 'add_node error: no such index'

#print methods
	#returns list of values 
	def listify(self):
		current_node = self.head_node
		lst = []

		while current_node:
			lst.append(current_node.get_value())
			current_node = current_node.get_next_node()
		return lst


			






#search methods
	def search_by_value(self, value):
		current_node = self.head_node
		idx = 0

		while current_node:
			if current_node.get_value() == value:
				return idx
			current_node = current_node.get_next_node()
			idx = idx + 1



n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
ll = LinkedList()
ll.add_node(n1)
ll.add_node(n2) ##
ll.add_node(n3, -1)
ll.add_node(n4) ##
ll.add_node(n5, -1)

##ll.delete_node(1) ##
#ll.delete_by_value(3)

#ll.delete_head_node()
#ll.delete_tail_node()

#print(ll.search_by_value(1))

print(ll.head_node.get_value())
print(ll.tail_node.get_value())

print(ll.listify())


## neveikia
# veikia

#tail nodai pjauna gryba, automatiskai nenusistato tail nodas kai sukuri lista, todel neveikia delete_tail metodas