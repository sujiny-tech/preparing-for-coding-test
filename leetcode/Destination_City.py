import collections

paths= [["pYyNGfBYbm","wxAscRuzOl"],["kzwEQHfwce","pYyNGfBYbm"]]#[["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]

def destCity(paths):
    route=collections.defaultdict(list)
    for start, dest in paths:
        route[start].append(dest)
    while paths:
        start, destination=paths.pop(0)
        if route[destination]==[]:
            return destination

    return destination

print(destCity(paths))