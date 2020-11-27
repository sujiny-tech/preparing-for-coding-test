heights=[5,1,2,3,4]#[1,1,4,2,1,3]

def heightChecker(heights):
    #solution 1.
    #sort_h=sorted(heights)
    #check=[sort_h[i]==heights[i] for i in range(len(heights))]
    #return check.count(False)

    #solution 2.
    sort_h=sorted(heights)
    ans=0
    for i in range(len(heights)):
        if heights[i]!=sort_h[i]:
            ans+=1
    return ans

print(heightChecker(heights))