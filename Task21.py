import sys


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

if __name__ == '__main__':
    input_function()