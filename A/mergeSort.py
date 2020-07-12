def mergeSort(l1):
    n=len(l1)
    if n>1:
        mid=n//2
        L=l1[:mid]
        R=l1[mid:]
        mergeSort(L)
        mergeSort(R)
        i=j=k=0
        while i<len(L) and j<len(R):
            if L[i]<R[j]:
                l1[k]=L[i]
                i+=1
            else:
                l1[k]=R[j]
                j+=1
            k+=1
        while i<len(L):
            l1[k]=L[i]
            i+=1
            k+=1
        while j<len(R):
            l1[k]=R[j]
            j+=1
            k+=1

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
mergeSort(my_list)
print("After Sorting ")
print_list(my_list)
