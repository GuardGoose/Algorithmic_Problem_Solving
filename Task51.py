from ast import literal_eval
import sys
import math

class Node:
    def __init__(self, value, left=None, right=None):
        self.data = value
        self.left = left
        self.right = right

    def leaf(self):
        return self.right is None and self.left is None

def build_kd_tree(kdtree, depth=0):
    try:
        # needed to check when there are singletons
        depth_space = len(kdtree[0])

    # These are just to catch any errors that
    # may stop the program
    except TypeError:
        pass
    except IndexError:
        return kdtree[1:]
    # Takes the length of the KDtree
    # and if it's even reduces the length by 1
    if len(kdtree) % 2 == 0:
        length = len(kdtree) - 1
    else:
        length = len(kdtree)
    # takes the median of the tree.
    median = int(length // 2)
    # Returns the KD tree.
    return Node(
        kdtree[median],
            build_kd_tree(kdtree[:median], depth + 1),
            build_kd_tree(kdtree[median + 1:], depth + 1)
    )

def intersect(minMax1, minMax2):
    for data in range(0, int(sys.stdin.readline().split())):
        if not (minMax2[0][data] <= minMax1[0][data] <= minMax2[1][data] or
                minMax2[0][data] <= minMax1[1][data] <= minMax2[1][data] or
                minMax1[0][data] <= minMax2[0][data] <= minMax1[1][data] or
                minMax1[0][data] <= minMax2[1][data] <= minMax1[1][data]):
            return False
    return True

def fully_contained(region, x, y, d):
    # in the range of all dimensions
    for data in range(0, int(d)):
        # if x and y are not in the region
        # then False is returned
        if not (int(x[data]) <= int(region[data]) <= int(y[data])):
            return False
    return True

def search_kdtree(data, x, y, d):
    # If the left is not empty
    if data.left != []:
        # checks to see if it's fully contained
        if fully_contained(data.left.data, x, y, d):
            # if True than it appends it to the answer
            answer.append(data.left.data)
        # then recursively calls on the function
        # to search until the list is empty
        search_kdtree(data.left, x, y, d)
    # if the right is not empty
    if data.right != []:
        # checks to see if the vaules are fully contained
        if fully_contained(data.right.data, x, y, d):
            # if True then appends to the answer
            answer.append(data.right.data)
        # then recursively calls on the function
        # to search until the list is empty
        search_kdtree(data.right, x, y, d)

def input_function():
        # Initalises the lists
    query_values = []
    input_list = []
    # Takes the input for list size, dimensions and number
    # of queries
    list_size, dimensions, no_queries = sys.stdin.readline().strip().split(" ")
    # Loop is executed in range of list_size
    for i in range(int(list_size)):
        # Takes the input and adds to the list
        lst = sys.stdin.readline().strip().split(" ") 
        input_list.append(lst)  
    # Loop is executed in range of no_queries
    for i in range(int(no_queries)):
        # Replaces the blank spaces with commas, so "literal_eval"
        # can be used.
        # Literal Eval just makes sure the input is a valid datatype.
        # If it isn't then it rasies an error
        lst2 = input().replace(" ", ", ")
        query_values.append(literal_eval(lst2))
    #query_values1 = [[int(y) for y in x] for x in query_values]
    #print(input_list)  # DEBUG
    #print(dimensions)  # DEBUG
    #print(query_values)# DEBUG
    # Returns the values
    return input_list, dimensions, query_values

if __name__ == "__main__":
    input_list, dimensions, query_values = input_function()
    # I am groot
    groot = build_kd_tree(input_list)
    # Takes two points at a time
    for x, y in query_values:
        answer = []
        # If returns True
        # then it's added to the list
        if fully_contained(groot.data, x, y, dimensions[0]):
            answer.append(groot.data)
            answer.sort()   # list is sorted
        search_kdtree(groot, x, y, dimensions[0])
        for i in answer:    # prints the answer
            print((str(i).replace(",", "")),end=' ')