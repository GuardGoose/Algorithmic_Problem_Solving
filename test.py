import sys

def two_one(storage, rng):
    storage.sort()

    if len(storage) == 1 and storage[0] in range(rng[0], rng[1]+ 1):
        return storage[0]
    if len(storage) == 0:
        return
    median_p = storage[len(storage)//2]
    ll = storage[:storage.index(median_p)]
    lr = storage[storage.index(median_p)+ 1:]
    if median_p in range(rng[0], rng[1] +1):
        return median_p, two_one(ll, rng), two_one(lr, rng)

    elif median_p < (rng[0]):
        return two_one(lr, rng)

    elif median_p > (rng[1]):
        return two_one(ll, rng)

my_input = sys.stdin.readline().split()
lst_0 = []

for rows in range(int(my_input[0])):
    lst_0.append(int(sys.stdin.readline()))


lst_rng = []

for i in range(int(my_input[1])):
    lst_rngs = sys.stdin.readline().split()
    lst_rng.append(lst_rngs)
    lst_rng[i] = [int(x) for x in lst_rng[i]]


for m in range(int(my_input[1])):
    my_tree = str(two_one(lst_0, lst_rng[m])).replace(" None", "").replace(")", '').replace("(", '').replace(",", "")
    print(my_tree)