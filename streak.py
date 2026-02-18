# ch = input("Enter a character: ")
# if ch in "aeiouAEIOU":
#     print("Vowel")
# else:
# 
#     print("Consonant")

#     #palindrome num
# num = int(input("Enter a number: "))
# temp = num
# rev = 0
# while num > 0:
#     digit = num % 10
#     rev = rev * 10 + digit
#     num = num // 10
# if temp == rev:
#     print("Palindrome number")
# else:
#     print("Not a palindrome")

# #palindrome string
# text = input("Enter a string: ")
# if text == text[::-1]:
#     print("Palindrome string")
# else:
#     print("Not a palindrome")

# #prime number
# num = int(input("Enter a number: "))
# flag = 0
# if num > 1:
#     for i in range(2, num):
#         if num % i == 0:
#             flag = 1
#             break
#         if flag == 0:
#          print("Prime number")
#     else:
#         print("Not a prime number")
# else:
#     print("Not a prime number")

# #armstrong num
# num = int(input("Enter a number: "))
# temp = num
# sum = 0
# while num > 0:
#     digit = num % 10
#     sum = sum + digit**3
#     num = num // 10
# if temp == sum:
#     print("Armstrong number")
# else:
#     print("Not an Armstrong number")

# #fibonacci series
# n = int(input("Enter number of terms: "))
# a, b = 0, 1
# for i in range(n):
#     print(a, end=" ")
#     a,b = b,a+b
    

#    #sum of digits
# num = int(input("Enter number: "))
# sum = 0
# while num > 0:
#     sum += num % 10
#     num //= 10
# print("Sum of digits:", sum)
 
# #largest of three numbers
# a = int(input())
# b = int(input())
# c = int(input())
# largest = max(a, b, c)
# print("Largest:", largest)

# #days in a week
# days = ["Monday", "Tuesday", "Wednesday", "Thursday",
#         "Friday", "Saturday", "Sunday"]
# for day in days:
#     print(day)
# #months in a year
# months = ["January", "February", "March", "April", "May", "June",
#           "July", "August", "September", "October", "November", "December"]
# for month in months:
#     print(month)
  
#   #to display month name using number
# month = int(input("Enter month number: "))
# months = ["January", "February", "March", "April", "May", "June",
#           "July", "August", "September", "October", "November", "December"]
# if 1 <= month <= 12:
#     print("Month is:", months[month - 1])
# else:
#     print("Invalid input")


# #find the largest of three numbers
# a = int(input())
# b = int(input())
# c = int(input())
# if a >= b and a >= c:
#     print(a)
# elif b >= c:
#     print(b)
# else:
#     print(c)

#    #simple prime number

# n = int(input())
# flag = True
# if n <= 1:
#     flag = False
# else:
#     for i in range(2, n):
#         if n % i == 0:
#             flag = False
#             break
# if flag:
#     print("Prime")
# else:
#     print("Not Prime")
 
# #swapping of two nums

# a = int(input())
# b = int(input())
# a, b = b, a
# print(a, b)

# name = input("Enter your name: ")
# print("Hello", name)

# for i in range(1, 6):
#     print(i)



# #fibonacci series
# n = int(input("Enter number of terms: "))
# a, b = 0, 1
# print("Fibonacci Series:")
# for i in range(n):
#     print(a, end=" ")
#     a, b = b, a + b


# #recursive fibonacci program
# def fibonacci(n):
#     if n <= 1:
#         return n
#     return fibonacci(n - 1) + fibonacci(n - 2)
# n = int(input("Enter number of terms: "))
# print("Fibonacci Series:")
# for i in range(n):
#     print(fibonacci(i), end=" ")


# #fiboonaci series vth loop method
# def fibonacci(n):
#     a, b = 0, 1
#     for _ in range(n):
#         print(a, end=" ")
#         a, b = b, a + b

# n = int(input("Enter number of terms: "))
# fibonacci(n)

# #lists
# lst = [10, 20, 30, 40]
# print("Max:", max(lst))
# print("Min:", min(lst))


# #number guessing game
# import random
# num = random.randint(1, 10)
# guess = int(input("Guess number (1-10): "))
# if guess == num:
#     print("Correct!")
# else:
#     print("Wrong! Number was:", num)

#file handlingg
with open("data.txt", "w") as f:
    f.write("Python streak day 9")

with open("data.txt", "r") as f:
    print(f.read())

#dictionary example

student = {"name": "Harshitha", "age": 18, "course": "Python"}
print(student["name"])


import random
num = random.randint(1, 25)
guess = int(input("Guess number (1-254): "))
if guess == num:
    print("Correct!")
else:
    print("Wrong! Number was:", num)
    
#inheritance example

class A:
    def show(self):
        print("Class A")
class B(A):
    def display(self):
        print("Class B")
obj = B()
obj.show()
obj.display()

#suduko solver

def solve(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for n in range(1, 10):
                    if valid(board, i, j, n):
                        board[i][j] = n
                        if solve(board):
                            return True
                        board[i][j] = 0
                return False
    return True

def valid(board, row, col, num):
    if num in board[row]:
        return False
    for i in range(9):
        if board[i][col] == num:
            return False
    sr, sc = (row//3)*3, (col//3)*3
    for i in range(sr, sr+3):
        for j in range(sc, sc+3):
            if board[i][j] == num:
                return False
    return True

#prime numbers blw two numbers

a, b = map(int, input("Enter range: ").split())
for n in range(a, b+1):
    if n > 1:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                break
        else:
            print(n, end=" ")


#simple calculator 

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("1.Add  2.Sub  3.Mul  4.Div")
choice = int(input("Choose operation: "))
if choice == 1:
    print("Result =", a + b)
elif choice == 2:
    print("Result =", a - b)
elif choice == 3:
    print("Result =", a * b)
elif choice == 4:
    print("Result =", a / b)
else:
    print("Invalid choice")


#perfect number

num = int(input("Enter a number: "))
sum_val = 0
for i in range(1, num):
    if num % i == 0:
        sum_val += i
if sum_val == num:
    print("Perfect Number")
else:
    print("Not Perfect Number")
