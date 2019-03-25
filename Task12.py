import sys
import bisect

class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

def balanced_tree(arr):
	if not arr:
		return

	# find middle
	mid = (len(arr)) // 2
	mid = int(mid)

	# make the middle element the root
	root = Node(arr[mid])

	# left subtree of root has all
	# values < arr[mid]
	root.left = balanced_tree(arr[:mid])

	# right subtree of root has all
	# values > arr[mid]
	root.right = balanced_tree(arr[mid + 1:])
	return root

def input_string():
    c = 0   # Initalises a counter
    query_values = []   # Initalises an empty list
    input_list = [] # Initalises an empty list
    # Takes the input of standard list size and no of queries
    # on a single line, seperated by a space
    list_size, no_queries = sys.stdin.readline().strip().split(" ")
    # For loop is executed in the range of list_size
    for i in range(int(list_size)):
        # Takes the input of the list and adds it to a list
        input_list.extend(sys.stdin.readline().strip().split(" "))
        # Converts list from string to int
        input_list = [int(i) for i in input_list]
    #print(input_list)   # DEBUG
    # Creates sublists in the query_values where
    # the start, and stop values will be stored
    # e.g no_queries = 3, query_values = [[], [], []]
    query_values = [[] for i in range(int(no_queries))]
    for i in range(int(no_queries)):    # For the size of no_queries
        start, stop = sys.stdin.readline().strip().split(" ")
        # Start and stop get added to a sublist.
        query_values[c].append(start)
        query_values[c].append(stop)
        # Changes to integers
        query_values[c] = [int(x) for x in query_values[c]]
        # Increments by 1 so sepereate queries get
        # added to sepereate sublists
        c += 1
    #print(query_values) #DEBUG
    return query_values, input_list

def find_range(items, values):
	start = bisect.bisect_left(items, values[0])
	end = bisect.bisect_right(items, values[1])
	return items[start:end]

def inorder_traversal(root):
	lst = []
	if root:
		lst = inorder_traversal(root.left)
		lst.append(root.data)
		lst = lst + inorder_traversal(root.right)
	return lst
	

def main():
	c = 0
	query_values, input_list = input_string()
	input_list.sort()
	root = balanced_tree(input_list)
	groot = inorder_traversal(root)
	for i in query_values:
		intervals = find_range(groot, query_values[c])
		c += 1
		print(intervals)	



if __name__ == '__main__':
	main()








