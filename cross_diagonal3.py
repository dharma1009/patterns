n = 9
for i in range(1,n+1,1):
    for j in range(1,n+1,1):
        if(j==1 or i== 9 or i==j):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()