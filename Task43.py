from ast import literal_eval
import sys

"""
This folder implementes the BuildKDTree algorithm, but it only
builds and prints the tree, the task only says to implement
the algorithm.

"""


class Node:
    def __init__(self, value, left=None, right=None):
        self.data = value
        self.left = left
        self.right = right


def BuildKDTree(kdtree, depth=0):
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
            BuildKDTree(kdtree[:median], depth + 1),
            BuildKDTree(kdtree[median + 1:], depth + 1)
    )

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
    # Returns the values
    return input_list, query_values

def main():
    value, query = input_function()
    value.sort()
    groot = BuildKDTree(value)
    # Prints the tree
    print(groot.data)
    print(groot.left.data, groot.right.data)
    print(groot.left.left.data, groot.left.right.data, groot.right.left.data, groot.right.right.data)

if __name__ == "__main__":
    main()