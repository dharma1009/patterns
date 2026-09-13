n = 5
for i in range(1,n+1,1):
    x = 1
    for j in range(1,i-1+1,1):
        print(x,end=" ")
        x+=1
    x=i
    for j in range(1,n-i+n-i+1+1,1):
        print(x,end=" ")
    x=i-1
    for j in range(1,i-1+1,1):
        print(x,end=" ")
        x-=1
    print()
n = 4
for i in range(1,n+1,1):
    y =1
    for j in range(1,n-i+1,1):
        print(y,end=" ")
        y+=1
    y =n-i+1
    for j in range(1,i+i+1+1,1):
        print(y,end=" ")
    y =n-i
    for j in range(1,n-i+1,1):
        print(y,end=" ")
        y-=1
    print()