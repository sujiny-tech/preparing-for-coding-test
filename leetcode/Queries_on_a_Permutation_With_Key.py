queries=[3,1,2,1]
m=5

def processQueries(queries, m):
    p=[x+1 for x in range(m)]
    ans=[]

    while queries:
        query=queries.pop(0)
        ind_p=p.index(query)
        ans.append(ind_p)

        p_val=p.pop(ind_p)
        p=[p_val]+p

    return ans

print(processQueries(queries, m))