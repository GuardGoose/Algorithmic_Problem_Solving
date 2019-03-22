class Node:
	def __init__(self, value):
		self.right = None
		self.left = None
		self.data = value

	def insertion(root, node):
		if root is None:
			node == root
		else:
			if root.data > node.data:
				if root.left is None:
					root.left = node
				else:
					binary_insert(root.left, node)
			else:
				if root.right is None:
					root.right = node
				else:
					binary_insert(root.right, node)
def pre_order_print(root):
	if not root:
		return
	print(root.data)
	pre_order_print(root.left)
	pre_order_print(root.right)



l = [1, 2, 3, 4, 5, 6]
insertion(l)
