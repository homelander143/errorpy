n=int(input("Enter the number of lines : "))
for i in range(n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(i+1):
        print("*  ",end=" ")
    print()