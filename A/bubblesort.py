def bubbleSort(l1):
    n=len(l1)
    for i in range(n):
        for j in range(0,n-i-1):
            if l1[j]>l1[j+1]:
                l1[j],l1[j+1]=l1[j+1],l1[j]

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
bubbleSort(my_list)
print("After Sorting ")
print_list(my_list)
