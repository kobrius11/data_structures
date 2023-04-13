


class TreeNode:
	def __init__(self, value):
		self.value = value
		self.children = []

	def add_child(self, node):
		self.children.append(node)
		return f"added child: {node.value}, to parrent {self.value} "

	def remove_child(self, node):
		self.children.pop(node)
		return f"removed child: {node.value} from parent {self.value}"

	def traverse(self):
		nodes_to_visit = [self]
		while len(nodes_to_visit) > 0:
			current_node = nodes_to_visit.pop()
			print(current_node.value)
			nodes_to_visit += current_node.children

#depth_first_search algorithm, O(n) 
def dfs_recursive(root, target, path= ()):
	path = path + (root,)

	if root.value == target:
		return path

	for child in root.children:
		path_found = dfs_recursive(child, target, path)
		if path_found:
			return path_found

	return None

def dfs_iterative(root, target):
	path = [root]
	while len(path) > 0:
		current_node = path.pop()
		if current_node.value == target:
			return path

		path += current_node.children



root = TreeNode("1")
first = TreeNode("2")
second = TreeNode("3")
root.add_child(first)
root.add_child(second)
third = TreeNode("4")
fourth = TreeNode("5")
first.add_child(third)
second.add_child(fourth)

print(dfs_iterative(root, "5"))
print(dfs_recursive(root, "5"))


