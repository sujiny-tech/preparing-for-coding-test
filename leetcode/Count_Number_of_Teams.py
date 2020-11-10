rating=[2,5,3,4,1]

def numTeams(rating):
    mid=0

    for i in range(len(rating)):
        for j in range(i+1, len(rating)):
            for k in range(j+1, len(rating)):
                if rating[i]<rating[j]<rating[k] or rating[i]>rating[j]>rating[k]:
                    mid+=1

    return mid

print(numTeams(rating))