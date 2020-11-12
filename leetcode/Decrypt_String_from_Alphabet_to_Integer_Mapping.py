s="10#11#12"

def freqAlphabets(s):
    table_1=[chr(97+x) for x in range(26)]
    list_s=[]

    i=0
    #string split
    while i<len(s):
        if s[i]=='#' :
            if list_s[-2]+list_s[-1]==s[i-2:i]:
                list_s.pop()
                list_s.pop()

            list_s.append(s[i-2:i])
        else:
            list_s.append(s[i])
        i+=1
        
    #mapping
    for i in range(len(list_s)):
        list_s[i]=table_1[int(list_s[i])-1]

    return ''.join(list_s)

print(freqAlphabets(s))