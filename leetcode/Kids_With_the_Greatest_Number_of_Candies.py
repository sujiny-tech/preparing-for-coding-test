candies=[2,3,5,1,3]
extraCandies=3

def kidsWithCandies(candies, extraCandies):
    #solution 1
    #answer=[]
    #for i in range(len(candies)):
    #    check=candies[i]+extraCandies
    #    max_candies=max(candies)
    #    if check>=max_candies:
    #        answer.append(True)
    #    else:
    #        answer.append(False)
    #return answer

    answer=[False]*len(candies)
    max_candies=max(candies)

    for i in rane(len(candies)):
        check=candies[i]+extraCandies
        if check>=max_candies:
            answer[i]=True

    return answer

print(kidsWithCandies(candies, extraCandies))
