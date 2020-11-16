startTime=[1,2,3]
endTime=[3,2,7]
queryTime=4

def busyStudent(startTime, endTime, queryTime):
    answer=0

    for start, end in zip(startTime, endTime):
        if start<=queryTime and queryTime<=end:
            answer+=1
    return answer

print(busyStudent(startTime, endTime, queryTime))