x=1534236469

def reverse(x):
    if x<0:
        x=str(x)[1:]
        x=int(x[::-1])
        x=x*(-1)
    else:
        x=str(x)[::-1]
        x=int(x)
    if x>=-(2**31) and x<=(2**31)-1:
        return x
    else:
        return 0

print(reverse(x))