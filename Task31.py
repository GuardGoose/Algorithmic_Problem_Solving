import sys

def matrix(input_list, d, querys):
    n =[]
    for point in input_list:
        c = 0
        for i in range(d):
            if querys[0] <= int(point) <= querys[1]:
                c += 1
    if c == d:
        n.append(point)
    return n

def input_function():
    c = 0   # Initalises a counter
    query_values = []   # Initalises an empty list
    input_list = [] # Initalises an empty list
    # Takes the input of standard list size and no of queries
    # on a single line, seperated by a space
    list_size, dimensions, no_queries = sys.stdin.readline().strip().split(" ")
    # For loop is executed in the range of list_size
    dimensions = [int(x) for x in dimensions[0]]
    if dimensions[0] == 1:
        for i in range(int(list_size)):
        # Takes the input of the list and extends it to a
        # single dimension array
            input_list.extend(sys.stdin.readline().strip().split(" "))
    elif dimensions[0] >= 2:
        for i in range(int(list_size)):
            # Takes the input of the list and extends it to a
            # multi dimension array
            input_list.append(sys.stdin.readline().strip().split(" "))
        # Converts list from string to int
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
    print(query_values) #DEBUG
    return query_values, dimensions, input_list

def main():
    query_values, dimensions, input_list = input_function()
    c = 0
    for i in query_values:
        groot = matrix(input_list, dimensions,query_values[c])
        c += 1

if __name__ == '__main__':
    main()