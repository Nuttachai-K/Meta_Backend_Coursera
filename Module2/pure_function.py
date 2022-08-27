my_list = [1,2,3]

def add_to_list(mList,item):
    tList = mList.copy()
    tList.append(item)
    return tList
print(add_to_list(my_list,4))

tList = str(my_list)
print(tList[0]+tList[2])
