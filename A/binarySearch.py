def binarySearch(l1,l,r,value):
    if r>=l:
        mid=l+(r-l)//2
        if l1[mid]==value:
            return mid
        elif l1[mid]>value:
            return binarySearch(l1,l,mid-1,value)
        else:
            return binarySearch(l1,mid+1,r,value)
    else:
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
res=binarySearch(my_list,0,len(my_list)-1,value)
if res==-1:
    print("Sorry Value Not Found..!")
else:
    print("{0} is found at {1} ".format(value,res))
