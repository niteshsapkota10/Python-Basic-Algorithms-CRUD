def linearSearch(list1,value):
    idx=-1
    for i in range(len(list1)):
        if value==list1[i]:
            idx=i
            break
        else:
            idx=-1
    return idx

def fill_list():
    list1=[]
    n=int(input("Enter the size of the List "))
    print("Enter List Elements ")
    for i in range(n):
        list1.append(int(input()))
    return list1

my_list=fill_list()
value=int(input("Enter Value to Search "))
res=linearSearch(my_list,value)
if res==-1:
    print("Sorry Value Not Found..!")
else:
    print("{0} is found at {1} ".format(value,res))