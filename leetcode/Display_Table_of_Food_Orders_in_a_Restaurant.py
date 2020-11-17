import collections
orders=[["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]

def displayTable(orders):
    ans=[["Table"]]
    menu_list=[]
    for order in orders:
        if order[2] in menu_list:
            continue
        else:
            menu_list.append(order[2])
    ans[0]+=sorted(menu_list)

    orders=sorted(orders, key=lambda x:int(x[1]))

    menu=collections.defaultdict(list)

    for order in orders:
        menu[order[1]].append(order[2])
    for c in menu.items():
        mid = ["0"] * len(ans[0])
        mid[0]=c[0] #table number

        menu_c=c[1]
        for menu_1 in menu_c:
            index_=ans[0].index(menu_1)
            mid[index_]=str(int(mid[index_])+1)

        ans.append(mid)

    return ans

print(displayTable(orders))