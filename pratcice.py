n = 5
for i in range(1,n+1,1):
    for j in range(1,n-i+1,1):
        print(" ",end=" ")
    x = i
    for j in range(1,i+1,1):
        print(x,end=" ")
        x-=1
    x = 2
    for j in range(1,i-1+1,1):
        print(x,end=" ")
        x+=1

    print()