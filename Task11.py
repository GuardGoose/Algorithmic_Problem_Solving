"""
Theta(n) time for both adding n items to the list, and for querying the list.
Implement your approach
using the input and output described in Task 2.1.
Call this file Task11.
"""

import sys


def search_list(list, start, stop):
    # This function is Theta(n**2)
    x = [y for y in list in range(int(start), int(stop) + 1)]
    sys.stdout.write(str(x))
    sys.stdout.flush()

def main():
    a = []
    j = sys.stdin.readline().strip().split(" ")
    j1 = ''.join(j)
    for i in range(int(j1)):    
        for line in sys.stdin.readline().strip().split(" "):
            a.append(line)
    print(a)    # DEBUG
    start, stop = sys.stdin.readline().strip().split(" ")
    search_list(a, start, stop)



if __name__ == '__main__':
    main()
