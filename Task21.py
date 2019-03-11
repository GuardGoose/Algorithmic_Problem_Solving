import sys


def one_d_range(tree, interval1, interval2):
    if not tree:
        return None
    tree = sorted(tree, key=int)
    tree_len = len(tree)
    interval = range(int(interval1), int(interval2) + 1)
    if tree_len == 1 and tree[0] in interval:
        return tree[0]
    if tree_len < 1:
        return None
    tredian = tree[tree_len // 2]
    left_leaf = tree[:tree.index(tredian)]
    right_leaf = tree[tree.index(tredian):]
    if tredian in interval:
        return tredian, one_d_range(left_leaf, interval1, interval2), one_d_range(right_leaf, interval1, interval2)
    elif tredian < interval1:
        return one_d_range(right_leaf, interval1, interval2)
    elif tredian > interval2:
        return one_d_range(left_leaf, interval1, interval2)
        
    
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
    #print(query_values) #DEBUG
    return query_values, input_list
    
    
def main():
    query_values, input_list = input_function()
    print(query_values)
    c = 0
    for i in query_values:
        print(query_values[c])
        x, y = query_values[c]
        groot = one_d_range(input_list, x, y)
        print(groot)
        c +=1

    
if __name__ == '__main__':
    main()