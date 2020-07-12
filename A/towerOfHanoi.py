def move(n,source,dest,spare):
    if n==1:
        print("Move from {0} to {1}".format(source,dest))
    else:
        move(n-1,source,spare,dest)
        move(1,source,dest,spare)
        move(n-1,spare,dest,source)

n=int(input("Enter the no of rings "))
move(n,'A','C','B')