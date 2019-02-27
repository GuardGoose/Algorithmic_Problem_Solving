import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def array_to_bst(array):
    if not array:
        return None
    
    # sorts the array as integer
    array = sorted(array, key=int)
    
    # find mid
    mid = (len(array)) / 2
    mid = int(mid)
    
    # make middle element the root
    root = Node(array[mid])
    
    # left subtree root has all
    # values < array[mid]
    root.left = array_to_bst(array[:mid])
    
    # right subtree of root has all
    # values > array[mid]
    root.right = array_to_bst(array[mid + 1:])
    # returns the root
    return root
    
    
    
def input_function():
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
    print(input_list)   # DEBUG
    # Creates sublists in the query_values where
    # the start, and stop values will be stored
    # e.g no_queries = 3, query_values = [[], [], []]
    query_values = [[] for i in range(int(no_queries))]
    for i in range(int(no_queries)):    # For the size of no_queries
        start, stop = sys.stdin.readline().strip().split(" ")
        # Start and stop get added to a sublist.
        query_values[c].append(start)
        query_values[c].append(stop)
        # Increments by 1 so sepereate queries get
        # added to sepereate sublists
        c += 1
    print(query_values) #DEBUG
    return input_list, query_values
    
def main():
    input_function()

    
if __name__ == '__main__':
    main()