import collections
arr=[1,2,2,1,1,3]

def uniqueOccurrences(arr):
    table=collections.Counter(arr)
    cnt=[]

    for val in table.values():
        if val not in cnt:
            cnt.append(val)
        else:
            return False

    return True

print(uniqueOccurrences(arr))