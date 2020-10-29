input_="2*3-4*5"

def diffWaysToCompute(input_):
    def compute(val, left, right):
        results=[]
        for l in left:
            for r in right:
                if val=="+":
                    results.append(int(l)+int(r))
                elif val=="-":
                    results.append(int(l)-int(r))
                else:
                    results.append(int(l)*int(r))
                #results.append(eval(str(l)+val+str(r)))
        return results
        
    if input_.isdigit():
        return [int(input_)]

    results=[]
    for index, val in enumerate(input_):
        if val in "+-*":
            left=diffWaysToCompute(input_[:index])
            right=diffWaysToCompute(input_[index+1:])
            #print(compute(val, left, right))
            results+=compute(val, left, right)
    
    return results

print(diffWaysToCompute(input_))
