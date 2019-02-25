"""
Theta(n) time for both adding n items to the list, and for querying the list.
Implement your approach
using the input and output described in Task 2.1.
Call this file Task11.
"""
import sys

def list_interval(list1, start, stop):
    # This function is Theta(n)
    answer = [] # Initalises a empty list
    for elem in list1:
        # If the element is between or equal to
        # start or stop then it's appended to the list
        if start <= int(elem) <= stop:
            answer.append(elem)
    # List is printed
    sys.stdout.write(str(answer))
    sys.stdout.flush()
            
def input_string():
    # Function is currently Theta(n)
    a = []  # Initialises an empty list
    # r respresents the size of the list
    r = sys.stdin.readline().strip().split(" ")
    # Adds r to r1
    r1 = ''.join(r)
    # Input a value for the size of r1
    # e.g. if r = 3, then the list would contain 3 elements
    # e.g. [1, 2, 3]
    for i in range(int(r1)):
        a.extend(sys.stdin.readline().strip().split(" "))
    print(a)    # DEBUG
    # This take the range for which the elements will be searched.
    start, stop = sys.stdin.readline().strip().split(" ")
    start = int(start)
    stop = int(stop)
    list_interval(a, start, stop)

def main():
    input_string()

if __name__ == '__main__':
    main()
