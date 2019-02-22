"""
Theta(n) time for both adding n items to the list, and for querying the list.
Implement your approach
using the input and output described in Task 2.1.
Call this file Task11.
"""
import sys

def search_list(list1, start, stop):
    # This function is Theta(n)
    answer = []
    range2 = range(start, (stop + 1))
    # compare = []
    # compare.append(range(start, (stop + 1)))
    for elem in list1:
        if start <= int(elem) <= stop:
            answer.append(elem)
    print(answer)
            
def main():
    # Function is currently Theta(n)
    a = []  # Initialises an empty list
    # r respresents the size of the list
    r = sys.stdin.readline().strip().split(" ")
    # Adds r to r1
    r1 = ''.join(r)
    # Input a value for the size of r1
    # e.g. if r = 3, then the list would contain 3 elements
    # e.g [1, 2, 3]
    for i in range(int(r1)):
        # This creates the list
        a.extend(sys.stdin.readline().strip().split(" "))
    print(a)    # DEBUG
    # This take the range for which the elements will be searched.
    start, stop = sys.stdin.readline().strip().split(" ")
    start = int(start)
    stop = int(stop)
    search_list(a, start, stop)



if __name__ == '__main__':
    main()
