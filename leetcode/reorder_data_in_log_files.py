logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
#logs.sort()
#print(logs)
d=[]
l=[]
for log in logs:
    if log.split()[1].isdigit():
        d.append(log)
    else:
        l.append(log)
l.sort(key=lambda x: (x.split()[1:], x.split()[0]))
print(l+d)
