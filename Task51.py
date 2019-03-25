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
        depth_space = len(kdtree[0])
        kdtree.sort()
    except TypeError:
        pass
    except IndexError:
        return kdtree[1:]
    if len(kdtree) % 2 == 0:
        length = len(kdtree) - 1
    else:
        length = len(kdtree)
    median = int(length // 2)
    return Node(
        kdtree[median],
        build_kd_tree(kdtree[:median], depth + 1),
        build_kd_tree(kdtree[median + 1:], depth + 1),
        )

def intersect(minMax1, minMax2):
    for data in range(0, int(sys.stdin.readline().split())):
        if not (minMax2[0][data] <= minMax1[0][data] <= minMax2[1][data] or
                minMax2[0][data] <= minMax1[1][data] <= minMax2[1][data] or
                minMax1[0][data] <= minMax2[0][data] <= minMax1[1][data] or
                minMax1[0][data] <= minMax2[1][data] <= minMax1[1][data]):
            return False
    return True

def fully_contained(region, x, y):
    for data in range(0, int(dimensions)):
        if not (x[data] <= region[data] <= y[data]):
            return False
    return True

def search_kdtree(data, x, y):
    if data.left != []:
        if fully_contained(data.left.data, x, y):
            report.append(data.left.data)
        search_kdtree(data.left, x, y)
    if data.right != []:
        if fully_contained(data.right.data, x, y):
            report.append(data.right.data)
        search_kdtree(data.right, x, y)

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
    return input_list, dimensions, query_values

def main():
    input_list, dimensions, query_values = input_function()
    groot = build_kd_tree(input_list)
    for x, y in query_values:
        answer = []
        if fully_contained(groot.data, x, y):
            answer.append(tree.data)
            answer.sort()
        search_kdtree(groot, x, y)
        for i in answer:
            print((str(i).replace(",", "")),end=' ')
        if answer:
            print('Pass')
        else:
            print("No pass")



if __name__ == "__main__":
    main()