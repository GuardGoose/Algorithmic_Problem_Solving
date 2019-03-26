import sys
<<<<<<< HEAD
from ast import literal_eval

def matrix(input_list, x, y, dimensions):
	n = []
	for x in input_list:
		c = 0
		for i in range(int(dimensions)):
			if int(x[i]) <= int(x[i]) <= int(y[i]):
				c+= 1
		if c == int(dimensions):
			n.append(x)
	return n


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
=======

def matrix(input_list, d, querys):
    n =[]
    for point in input_list:
        c = 0
        for i in range(d):
            if querys[0] <= int(point) <= querys[1]:
                n.append(point)
                c += 1
    if c == d:
        n.append(point)
    print(n)

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
    print(dimensions)   # DEBUG
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
>>>>>>> 0f9869ebee2a1deb31bc29982ef2562dff03a59b
    return query_values, dimensions, input_list

def main():
    query_values, dimensions, input_list = input_function()
<<<<<<< HEAD
    #print(query_values[0])
    #str(query_values[1]
    for x, y in query_values:
    	print(str(matrix(input_list, x, y, dimensions)))
=======
    c = 0
    for i in query_values:
        groot = matrix(input_list, dimensions[0],query_values[c])
        c += 1
>>>>>>> 0f9869ebee2a1deb31bc29982ef2562dff03a59b

if __name__ == '__main__':
    main()