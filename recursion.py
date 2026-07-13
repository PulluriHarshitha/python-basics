#recursion 1 to n numbers
# def print_numbers(n, i=1):
#     if i > n:
#         return
#     print(i)
#     print_numbers(n, i + 1)
# n = int(input())
# print_numbers(n)

# def num(n):
#     if n==0:
#         return
#     print(n,end=" ")
#     num(4)

#sum of digits of a number using recursion
# def sumD(n):
#     if n==0:
#         return 0
#     return n%10+sumD(n//10)
# print(sumD(1234))  #1+2+3+4=10   

#counting the number of digits in a number using recursion
# def countD(n):
#     if n==0:
#         return 0
#     return 1+countD(n//10)
# print(countD(1234567890))  #10 digits