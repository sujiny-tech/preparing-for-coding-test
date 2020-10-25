import collections

s="bcabc"
s="cbacdcbc"
#중복된 문자 제거, 사전식 순서로 나열.
#stack -> 나중에 들어온거 후입선출.
#b  pop해서 넣고, 그다음꺼랑 비교하고, 없으면 또 push해주고
#bca 까지 넣고, 이 안에 그다음거 있는지
#output=[]
#element=[]
#min_=s.index(min(s))
#print(s[min_:])
'''
def removeDup(s:str)->str:
    for char in sorted(set(s)):
        suffix=s[s.index(char):]
        if set(s)== set(suffix):
            return char+removeDup(suffix.replace(char, ''))
    return ''
print(removeDup(s))
'''
counter, seen, stack=collections.Counter(s), set(), []
print(counter)
for char in s:
    counter[char]-=1
    #집합에 char있으면 패스.
    if char in seen:
        continue
    #뒤에 붙일 문자가 남아있으면 스택에서 제거.
    while stack and char<stack[-1] and counter[stack[-1]]>0:
        print(char, stack[-1])
        seen.remove(stack.pop())
    #char을 스택에 추가하고, 집합에도 추가.
    stack.append(char)
    seen.add(char)
    print("stack :", stack)
    print("seen : ", seen)
print(''.join(stack))