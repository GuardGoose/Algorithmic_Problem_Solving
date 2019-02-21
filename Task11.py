"""
Delta(n) time for both adding n items to the list, and for querying the list.
Implement your approach
using the input and output described in Task 2.1.
Call this file Task11.
"""

import sys


def search_list(start, stop):
    temp = []
    for i in range(int(start), int(stop)+1):
        temp.append[i]
    sys.stdout.write(str(temp))
    sys.stdout.flush()

if __name__ == '__main__':
    a = []
    j = sys.stdin.readline().strip().split(" ")
    j1 = ''.join(j)
    for i in range(int(j1)):    
        for line in sys.stdin.readline().strip().split(" "):
            a.append(line)
    start, stop = sys.stdin.readline().strip().split(" ")
    search_list(start, stop)