n=4

def generateTheString(n):
    #solution 1.
    arr=[chr(x) for x in range(97, 122)]
    if n%2!=0:
        return arr.pop(0)*n
    else:
        return arr.pop(0)*(n-1)+arr.pop(0)*(1)

print(generateTheString(n))