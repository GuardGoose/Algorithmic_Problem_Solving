import sys

def one_d_range(tree, values):
    # Sorts the list
    tree = sorted(tree, key=int)
    if not tree:
        return None
    # Stored length of tree
    tree_len = len(tree)
    # Stored the range that's being sought out
    interval = range(values[0], (values[1] + 1))
    # If the tree has length of 1 and in the range
    # then just return the value
    if tree_len == 1 and tree[0] in interval:
        return tree[0]
    # If there aren't any values then
    # return None
    if tree_len == 0:
        return None
    # Takes the floor median of the tree
    tredian = tree[tree_len // 2]
    # Left leaf is leftmost value of from the median
    left_leaf = tree[:tree.index(tredian)]
    # Right leaf is right most
    # +1 to account for index = 0
    right_leaf = tree[tree.index(tredian) + 1:]
    # Last functions just check and return reported nodes.
    # It's recursive
    if tredian in interval:
        return tredian, one_d_range(left_leaf, values), one_d_range(right_leaf, values)
    elif tredian < values[0]:
        return one_d_range(right_leaf, values)
    elif tredian > values[1]:
        return one_d_range(left_leaf, values)
        
    
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
        # Converts list from string to int
        input_list = [int(i) for i in input_list]
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
        # Changes to integers
        query_values[c] = [int(x) for x in query_values[c]]
        # Increments by 1 so sepereate queries get
        # added to sepereate sublists
        c += 1
    #print(query_values) #DEBUG
    return query_values, input_list
    
    
def main():
    query_values, input_list = input_function()
    # Allow C to increment and navigate through the sublists
    c = 0
    # Iterate through sub-lists
    for i in query_values:
        #print(query_values[c]) # DEBUG
        # Make a string so I can replace all the brackets
        # and everything else to get the desired output
        # Note: Output is unsorted because I don't know how
        groot = str(one_d_range(input_list, query_values[c])).replace(" None", "").replace(")", '').replace("(", '').replace(",", "")
        # Prints Groot
        print(groot)
        # Increments to the next sublist
        c += 1

    
if __name__ == '__main__':
    main()