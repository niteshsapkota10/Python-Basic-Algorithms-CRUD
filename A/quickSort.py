def partition(l1,low,high):
    i=(low-1)
    pivot=l1[high]
    for j in range(low, high):
        if l1[j] < pivot:
            i=i+1
            l1[i],l1[j]=l1[j],l1[i]
    l1[i+1],l1[high]=l1[high],l1[i + 1]
    return (i+1)

def quickSort(l1,low,high):
    if low<high:
        pi=partition(l1,low,high)
        quickSort(l1,low,pi-1)
        quickSort(l1,pi+1,high)

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
n=len(my_list)
quickSort(my_list,0,n-1)
print("After Sorting ")
print_list(my_list)

