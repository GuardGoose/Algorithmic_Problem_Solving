import sys
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
    return query_values, dimensions, input_list

def main():
    query_values, dimensions, input_list = input_function()
    #print(query_values[0])
    #str(query_values[1]
    for x, y in query_values:
    	print(str(matrix(input_list, x, y, dimensions)))

if __name__ == '__main__':
    main()