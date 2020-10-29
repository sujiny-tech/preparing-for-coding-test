x, y=1, 4

def hammingDistance(x, y):
    return bin(x^y).count('1')

print(hammingDistance(x, y))
