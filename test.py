import bisect

data = [1,2,3,4,5,23,7,8,9,10,11,12,13]

def NumbersWithinRange(items, lower, upper):
    start = bisect.bisect_left(items, lower)
    end = bisect.bisect_right(items, upper)
    return items[start:end]

subset = NumbersWithinRange(data, 2,8)
print(subset)