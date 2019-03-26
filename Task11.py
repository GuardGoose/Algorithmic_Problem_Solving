"""
Theta(n) time for both adding n items to the list, and for querying the list.
Implement your approach
using the input and output described in Task 2.1.
Call this file Task11.
"""
import sys

def list_interval(list1, intervals):
    # This function is Theta(n)
    answer = [] # Initalises a empty list
    for elem in list1:
        # If the element is between or equal to
        # start or stop then it's appended to the list
        if intervals[0] <= int(elem) <= intervals[1]:
            answer.append(elem)
    # Lists are printed out on seperate lines.
    sys.stdout.write(str(answer) + '\n')
    sys.stdout.flush()
            
def input_string():
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
    #print(input_list)   # DEBUG
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
    query_values, input_list = input_string()
    c = 0 
    for i in query_values:
        list_interval(input_list, query_values[c])
        c += 1
    
    
if __name__ == '__main__':
    main()
