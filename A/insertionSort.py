def insertionSort(l1):
    n=len(l1)
    for i in range(1,n):
        key=l1[i]
        j=i-1
        while j>=0 and key<l1[j]:
                l1[j+1]=l1[j]
                j-=1
        l1[j+1]=key

def fill_list():
    list1=[]
    n=int(input("Enter the size of the List "))
    print("Enter List Elements ")
    for i in range(n):
        list1.append(int(input()))
    return list1

def print_list(l1):
    for i in l1:
        print(i)

my_list=fill_list()
print("Before Sorting : ")
print_list(my_list)
insertionSort(my_list)
print("After Sorting ")
print_list(my_list)
