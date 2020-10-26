import collections

s="bcabc"
s="cbacdcbc"

counter, seen, stack=collections.Counter(s), set(), []
print(counter)
for char in s:
    counter[char]-=1
    
    if char in seen:
        continue
        
    while stack and char<stack[-1] and counter[stack[-1]]>0:
        print(char, stack[-1])
        seen.remove(stack.pop())
    
    stack.append(char)
    seen.add(char)
    print("stack :", stack)
    print("seen : ", seen)
print(''.join(stack))
