def interpolationSearch(list1,n,value):
    lo=0
    hi=(n-1)
    while lo<=hi and value>=list1[lo] and value<=list1[hi]:
        if lo==hi:
            if list1[lo]==value:
                return lo;
            return -1;
        pos=lo+int(((float(hi-lo)/(list1[hi]-list1[lo]))*(value-list1[lo])))
        if list1[pos]==value:
            return pos

        if list1[pos]<value:
            lo=pos+1;
        else:
            hi=pos-1;
    return -1

def fill_list():
    list1=[]
    n=int(input("Enter the size of the List "))
    print("Enter List Elements ")
    for i in range(n):
        list1.append(int(input()))
    return list1

my_list=fill_list()
value=int(input("Enter Value to Search "))
res=interpolationSearch(my_list,len(my_list),value)
if res==-1:
    print("Sorry Value Not Found..!")
else:
    print("{0} is found at {1} ".format(value,res))