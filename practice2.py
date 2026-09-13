# def even_odd(n):
#     return n%2 ==0
# n = int(input("enter the input:"))
# flag = even_odd(n)
# if flag:
#     print("even number")
# else:
#     print("odd number")
# starting and ending range of the number
# def even_odd(n):
#     return n%2 ==0
# start = int(input("enter the starting number:"))
# end = int(input("enter the ending number:"))
# if start>end:
#     print("invlaid input")
# else:
#     for i in range(start,end+1):
#         flag = even_odd(i)
#         if flag:
#             print(i,end=" ")
# def even_odd(n):
#     return n%2 ==0
# start = int(input("enter the starting number:"))
# end = int(input("enter the ending number:"))
# if start>end:
#     print("invlaid number")
# else:
#     print("even number:")
#     for i in range(start,end+1):
#         flag = even_odd(i)
#         if flag:
#             print(i,end=" ")
#     print()
#     print("odd numbers")
#     for j in range(start,end+1):
#         flag = even_odd(j)
#         if not flag:
#             print(j,end=" ")

# def even_odd(n):
#     return n%2 ==0
# count = int(input("enter the count:"))
# series = 1
# print(f"the first {count}even number are:")
# while count>0:
#     flag = even_odd(series)
#     if flag:
#         print(series,end=" ")
#         count-=1
# #     series+=1

# def even_odd(n):
#     return n%2 ==0
# count = int(input("enter the number:"))
# series = 1
# print(f"the first{count} odd number are: ")
# while count>0:
#     flag = even_odd(series)
#     if not flag:
#         print(series,end=" ")
#         count-=1
#     series+=1
# print("reverse of a number:")
# def reverse_num(n):
#     temp = n
#     if n<=0:
#         n = n*-1
#     rev = 0
#     while n>0:
#         rem = n%10
#         rev = rev*10+rem
#         n = n//10
#     if temp<0:
#         rev = rev*-1
#     return rev
# n = int(input("enter the number"))
# res = reverse_num(n)
# print(f"the reversal of the {n} is",res)
# def reverse_num(n):
#     temp = n
#     if temp<=0:
#         n = n*-1
#     rev = 0
#     while n>0:
#         rem = n%10
#         rev = rev*10+rem
#         n = n//10
#     if temp<n:
#         rev =rev*-1
#     return rev
# start = int(input("enter the starting number:"))
# end = int(input("enter the ending number:"))
# if start>end:
#     print("invlaid")
# else:
#     for i in range(start,end+1):
#         res = reverse_num(i)
#         print(f"the reversal of {i} is :",res)

# def integerpalindrome(n):
#     temp = n
#     if n<=0:
#         n = n*-1
#     rev = 0
#     while n>0:
#         rem = n%10
#         rev = rev*10+rem
#         n = n//10
#     if temp<=0:
#         rev = rev*-1
#     return rev == temp
# n = int(input("enter the number"))
# flag = integerpalindrome(n)
# if flag:
#     print("integer palindrome")
# else:
#     print("not a integer palindrome")

# def integerpalindrome(n):
#     temp = n
#     if n<=0:
#         n =n*-1
#     rev = 0
#     while n>0:
#         rem = n%10
#         rev = rev*10+rem
#         n = n//10
#     if temp<=0:
#         rev = rev*-1
#     return temp == rev
# count = int(input("enter the number:"))
# series = 1
# print(f"the first {count} palindromic number are:")
# while count>0:
#     flag = integerpalindrome(series)
#     if flag:
#         print(series,end=" ")
#         count-=1
#     series+=1

# def count_digits(n):
#     if n<=0:
#         n = n*-1
#     count = 0
#     while n>0:
#         n = n//10
#         count = count+1
#     return count
# start  = int(input("enter the number:"))
# end = int(input("enter the number:"))
# if start>end:
#     print("invlaid input")
# else:
#     for i in range(start,end+1):
#         res = count_digits(i)
#         print(f"the digits present in {i}",res)
# print("armstrong number:")
# def countdigits(n):
#     if n<=0:
#         n =n*-1
#     count = 0
#     while n>0:
#         n = n//10
#         count = count+1
#     return count
# def armstongnumber(n):
#     temp = n
#     if n<=0:
#         n = n*-1
#     asn = 0
#     pow = countdigits(n)
#     while n>0:
#         base = n%10
#         asn = asn+(base**pow)
#         n = n//10
#     if temp<=0:
#         asn = asn*-1
#     return asn == temp
# n = int(input("enter the number:"))
# flag = armstongnumber(n)
# if flag:
#     print("Armstong number")
# else:
#     print("not a armstong number")

# def count_digits(n):
#     if n<=0:
#         n = n*-1
#     count = 0
#     while n>0:
#         n = n//10
#         count+=1
#     return count
# def armstong_number(n):
#     temp = n
#     if n<=0:
#         n =n*-1
#     asn = 0
#     pow = count_digits(n)
#     while n>0:
#         base = n%10
#         asn = asn+(base**pow)
#         n = n//10
#     if temp<=0:
#         asn = asn*-1
#     return temp == asn
# start = int(input("enter the starting number:"))
# end = int(input("enter the ending number:"))
# if start>end:
#     print("invlaid input:")
# else:
#     for i in range(start,end+1):
#         flag = armstong_number(i)
#         if not flag:
#             print(i,end=" ")

def count_digits(n):
    if n<=0:
        n = n*-1
    count = 0
    while n>0:
        n = n//10
        count+=1
    return count
def armstrong_number(n):
    temp = n
    if n<=0:
        n = n*-1
    asn = 0
    pow = count_digits(n)
    while n>0:
        base = n%10
        asn = asn+(base**pow)
        n = n//10
    if temp<=0:
        asn = asn*-1
    return temp == asn
count1 = int(input("enter the number:"))
series = 1
print("f the first {count1} armstong number are:")
while count1>0:
    flag = armstrong_number(series)
    if flag:
        print(series,end=" ")
        count1-=1
    series+=1



