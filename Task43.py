import sys
from statistics import median

def BuildKDTree(tree, depth=0):
    tree = sorted(tree, key=int)
    
    if len(tree) == 0:
        return
    
    elif len(tree) == 1:
        return tree[0]
    
    if len(tree) % 2 != 0:
        tredian = median(tree)
        
    else:
        tredian = median(tree[:-1])
        
    p_left = tree[:tree.index(tredian)]
    p_right = tree[tree.index(tredian) + 1:]
    v_left = BuildKDTree(p_left, depth + 1)
    v_right = BuildKDTree(p_right, depth + 1)
    return tredian, v_left, v_right

print(BuildKDTree([[12,3,2,4,643,232],[12,65,87,453,343],[6,5,3,0,2,3]]))