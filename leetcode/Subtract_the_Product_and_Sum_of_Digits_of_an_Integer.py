n=234

def subtractProductAndSum(n):
    product_=1
    sum_=0
    
    for n_ in list(str(n)):
        product_*=int(n_)
        sum_+=int(n_)
    return product_-sum_

print(subtractProductAndSum(n))
