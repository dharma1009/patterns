n =9
for i in range(1,n+1,1):
    for j in range(1,n+1,1):
        if(i==9 or j==9 or i+j ==n+1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()