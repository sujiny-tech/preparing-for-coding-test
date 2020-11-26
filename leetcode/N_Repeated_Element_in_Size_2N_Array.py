import collections
A=[2,1,2,5,3,2]

def repeatedNTimes(A):
    #solution 1. collections.Counter
    #table=collections.Counter(A)
    #return table.most_common(1)[0][0]
    
    #solution 2. sorting -> val[i]==val[i+1] -> return val[i]
    #A=sorted(A)
    #for i in range(len(A)-1):
    #    if A[i]==A[i+1]:
    #        return A[i]

    #solution 3. dictionary count
    cnt=collections.defaultdict(int)
    for i in range(len(A)):
        if cnt[A[i]]==0:
            cnt[A[i]]+=1
        else:
            return A[i]

print(repeatedNTimes(A))
