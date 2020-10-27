intervals=[[1,4],[0,1]]#[[1,3],[2,6],[8,10],[15,18]]

def merge(intervals):
    arr=[]
    intervals=sorted(intervals, key=lambda x:x[0])
    while intervals:
        inter=intervals.pop(0)
        if not arr:
            arr.append(inter)
        else:
            #arr
            arr_lst=arr.pop()
            if arr_lst[1]<inter[0]:
                arr.append(arr_lst)
                arr.append(inter)
            else:
                if arr_lst[1]>inter[0] and arr_lst[1]<inter[1]:
                    arr.append([arr_lst[0],inter[1]])
                elif arr_lst[1]==inter[0]:
                    arr.append([arr_lst[0], inter[1]])
                else:
                    arr.append(arr_lst)
    print(arr)
print(merge(intervals))