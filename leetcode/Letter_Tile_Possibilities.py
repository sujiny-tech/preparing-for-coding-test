import itertools

tiles="AAB"

def numTilePossibilities(tiles):
    all_=[]
    for i in range(1, len(tiles)+1):
        all_+=list(itertools.permutations(tiles,i))
    all_=list(set(all_))
    return len(all_)

print(numTilePossibilities(tiles))