import sys
 
numbers_list = []
limits = []
 
 
class Node:
    def __init__(self, value, left=None, right=None):
        self.v = value
        self.l = left
        self.r = right
 
    def is_leaf(self):
        return self.r is None and self.l is None
 
 
def BuildKDTree(P, d=0):
    try:
        d_space = len(P[0])
        # not needed
        axis = d % d_space
        P.sort()
 
    except TypeError:
        pass
    except IndexError:
        return P
 
    if len(P) % 2 == 0:
        median = int((len(P)-1) / 2)
    else:
        median = int(len(P) / 2)
 
    return Node(
                P[median],
                BuildKDTree(P[:median], d + 1),
                BuildKDTree(P[median + 1:], d + 1)
               )
 
 
def intersect(minMax1,minMax2):
    for d in range(0, D):
        if not (minMax2[0][d] <= minMax1[0][d] <= minMax2[1][d] or
                minMax2[0][d] <= minMax1[1][d] <= minMax2[1][d] or
                minMax1[0][d] <= minMax2[0][d] <= minMax1[1][d] or
                minMax1[0][d] <= minMax2[1][d] <= minMax1[1][d]):
            return False
    return True
 
 
def SearchKDTree(v, s, f):
    if v.l != []:
        if isFullyContained(v.l.v, s, f):
            report.append(v.l.v)
        SearchKDTree(v.l, s, f)
 
    if v.r != []:
        if isFullyContained(v.r.v, s, f):
            report.append(v.r.v)
        SearchKDTree(v.r, s, f)
 
 
def isFullyContained(region, s, f):
    for d in range(0, D):
        if not (s[d] <= region[d] <= f[d]):
            return False
    return True
 
 
def map_list():
    test = sys.stdin.readline().replace("[", '').replace("]", '').split()
    return list(map(int, test))
 
 
def input_lists(specs):
    # i never have the need to use D as long as input is correct
    for R in range(specs[0]):
        numbers_list.append(map_list())
 
    for Q in range(specs[2]):
        ph = input().replace(" ", ", ")
        limits.append(literal_eval(ph))
 
    return specs[1]
 
 
D = input_lists(map_list())
 
tree = BuildKDTree(numbers_list)
 
st = default_timer()
 
for s, f in limits:
    report = []
 
    if isFullyContained(tree.v, s, f):
        report.append(tree.v)
 
    SearchKDTree(tree, s, f,)
    for value in sorted(report):
        print((str(value).replace(",", "")), end=' ')
    if report:
        print('asd')
    else:
        print("No pass")