 ch = input("Enter a character: ")
# if ch in "aeiouAEIOU":
#        print("Vowel")
# else:
#        print("Consonant")

# #palindrome num
# num = int(input("Enter a number: "))
# temp = num
# rev = 0
# while num > 0:
#     digit = num % 10
#     rev = rev * 10 + digit
# num = num // 10
# if temp == rev:
#       print("Palindrome number")
# else:
#       print("Not a palindrome")

#  palindrome string
# text = input("Enter a string: ")
# if text == text[::-1]:
#      print("Palindrome string")
# else:
#    print("Not a palindrome")


# # #prime number
# num = int(input("Enter a number: "))
# flag = 0
# if num > 1:
#      for i in range(2, num):
#          if num % i == 0:
#              flag = 1
#              break
#          if flag == 0:
#           print("Prime number")
#      else:
#          print("Not a prime number")
# else:
#     print("Not a prime number")

# #armstrong num
# num = int(input("Enter a number: "))
# temp = num
# sum = 0
# while num > 0:
#      digit = num % 10
#      sum = sum + digit**3
#      num = num // 10
# if temp == sum:
#      print("Armstrong number")
# else:
#      print("Not an Armstrong number")

# ##fibonacci series
# n = int(input("Enter number of terms: "))
# a, b = 0, 1
# for i in range(n):
#     print(a, end=" ")
# a,b = b,a+b
    

#     #sum of digits
# num = int(input("Enter number: "))
# sum = 0
# while num > 0:
#     sum += num % 10
#     num //= 10
# print("Sum of digits:", sum)
 
#  #largest of three numbers
# a = int(input())
# b = int(input())
# c = int(input())
# largest = max(a, b, c)
# print("Largest:", largest)

# # #days in a week
# days = ["Monday", "Tuesday", "Wednesday", "Thursday",
#          "Friday", "Saturday", "Sunday"]
# for day in days:
#     print(day)

#  months in a year
# months = ["January", "February", "March", "April", "May", "June","July", "August", "September", "October", "November", "December"]
# for month in months:
#    print(month)
  
# to display month name using number
# month = int(input("Enter month number: "))
# months = ["January", "February", "March", "April", "May", "June","July", "August", "September", "October", "November", "December"]
# if 1 <= month <= 12:
#      print("Month is:", months[month - 1])
# else:
#     print("Invalid input")

# #find the largest of three numbers
# a = int(input())
# b = int(input())
# c = int(input())
# if a >= b and a >= c:
#      print(a)
# elif b >= c:
#     print(b)
# else:
#      print(c)

# ##simple prime number
# n = int(input())
# flag = True
# if n <= 1:
#      flag = False
# else:
#      for i in range(2, n):
#          if n % i == 0:
#              flag = False
#              break
# if flag:
#      print("Prime")
# else:
#      print("Not Prime")
 
# ##swapping of two nums

# a = int(input())
# b = int(input())
# a, b = b, a
# print(a, b)
# name = input("Enter your name: ")
# print("Hello", name)
# for i in range(1, 6):
#      print(i)



# ##fibonacci series
# n = int(input("Enter number of terms: "))
# a, b = 0, 1
# print("Fibonacci Series:")
# for i in range(n):
#    print(a, end=" ")
# a, b = b, a + b


# ##recursive fibonacci program
# def fibonacci(n):
#      if n <= 1:
#         return n
#      return fibonacci(n - 1) + fibonacci(n - 2)
# n = int(input("Enter number of terms: "))
# print("Fibonacci Series:")
# for i in range(n):
#      print(fibonacci(i), end=" ")


#  #fiboonaci series vth loop method
# def fibonacci(n):
#     a, b = 0, 1
#     for _ in range(n):
#         print(a, end=" ")
#         a, b = b, a + b
# n = int(input("Enter number of terms: "))
# fibonacci(n)

# ##lists
# list = [10, 20, 30, 40]
# print("Max:", max(list))
# print("Min:", min(list))


# ##number guessing game
# import random
# num = random.randint(1, 10)
# guess = int(input("Guess number (1-10): "))
# if guess == num:
#     print("Correct!")
# else:
#     print("Wrong! Number was:", num)


# #dictionary example

# student = {"name": "Harshitha", "age": 18, "course": "Python"}
# print(student["name"])


# import random
# num = random.randint(1, 25)
# guess = int(input("Guess number (1-254): "))
# if guess == num:
#     print("Correct!")
# else:
#     print("Wrong! Number was:", num)
    
# #inheritance example

# class A:
#     def show(self):
#         print("Class A")
# class B(A):
#     def display(self):
#         print("Class B")
# obj = B()
# obj.show()
# obj.display()

# #suduko solver
# def solve(board):
#     for i in range(9):
#         for j in range(9):
#             if board[i][j] == 0:
#                 for n in range(1, 10):
#                     if valid(board, i, j, n):
#                         board[i][j] = n
#                         if solve(board):
#                             return True
#                         board[i][j] = 0
#                 return False
#     return True
# def valid(board, row, col, num):
#     if num in board[row]:
#         return False
#     for i in range(9):
#         if board[i][col] == num:
#             return False
#     sr, sc = (row//3)*3, (col//3)*3
#     for i in range(sr, sr+3):
#         for j in range(sc, sc+3):
#             if board[i][j] == num:
#                 return False
#     return True

# #prime numbers blw two numbers
# a, b = map(int, input("Enter range: ").split())
# for n in range(a, b+1):
#     if n > 1:
#         for i in range(2, int(n**0.5)+1):
#             if n % i == 0:
#                 break
#         else:
#             print(n, end=" ")


# #simple calculator 

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# print("1.Add  2.Sub  3.Mul  4.Div")
# choice = int(input("Choose operation: "))
# if choice == 1:
#     print("Result =", a + b)
# elif choice == 2:
#     print("Result =", a - b)
# elif choice == 3:
#     print("Result =", a * b)
# elif choice == 4:
#     print("Result =", a / b)
# else:
#     print("Invalid choice")


# #perfect number
# num = int(input("Enter a number: "))
# sum_val = 0
# for i in range(1, num):
#     if num % i == 0:
#         sum_val += i
# if sum_val == num:
#     print("Perfect Number")
# else:
#     print("Not Perfect Number")


# #file handling-write and read
# with open("data.txt", "w") as f:
#     f.write("Hello Python")

# with open("data.txt", "r") as f:
#     print(f.read())


# #Merge Two Dictionaries
# d1 = {1: 10, 2: 20}
# d2 = {3: 30, 4: 40}
# d3 = {**d1, **d2}
# print(d3)


# #Remove Duplicate Characters
# s = input("Enter a string: ")
# result = ""
# for ch in s:
#     if ch not in result:
#         result += ch
# print("After removing duplicates:", result)


# #Find Second Largest Number in List
# lst = list(map(int, input("Enter numbers: ").split()))
# unique = list(set(lst))
# unique.sort()
# print("Second largest:", unique[-2])

# #Reverse Each Word in a Sentence
# s = input("Enter a sentence: ")
# words = s.split()
# rev = [w[::-1] for w in words]
# print(" ".join(rev))

# #Swap Two Numbers
# a = 100
# b = 200
# a, b = b, a
# print("a =", a, "b =", b)

# #Remove Duplicates from List
# lst = [1, 2, 2, 3, 4, 4, 5]
# print(list(set(lst)))

# #Find Missing Number in Array
# arr = [1, 2, 3, 5, 6]
# n = 6
# expected = n * (n + 1) // 2
# print("Missing =", expected - sum(arr))

# #simple atm machine
# balance = 5000
# while True:
#     print("\n1.Deposit  2.Withdraw  3.Check Balance  4.Exit")
#     choice = int(input("Enter choice: "))

#     if choice == 1:
#         amt = int(input("Enter deposit amount: "))
#         balance += amt
#     elif choice == 2:
#         amt = int(input("Enter withdraw amount: "))
#         if amt <= balance:
#             balance -= amt
#         else:
#             print("Insufficient Balance")
#     elif choice == 3:
#         print("Balance =", balance)
#     elif choice == 4:
#         break
#     else:
#         print("Invalid choice")


#         #find a missing array
# arr = [1, 2, 3, 5, 6]
# n = 6
# expected = n * (n + 1) // 2
# print("Missing =", expected - sum(arr))

# #example
# print("hello world");

# #EXAMPLE

# num = int(input("Enter a number: "))
# fact = 1
# for i in range(1, num + 1):
#     fact = fact * i
# print("Factorial =", fact) 

# #python reverse py
# num = int(input("Enter a number: "))
# rev = 0
# while num > 0:
#     digit = num % 10
#     rev = rev * 10 + digit
#     num = num // 10
# print("Reversed Number =", rev)

# #find largest nums
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# if a > b and a > c:
#     print("Largest =", a)
# elif b > c:
#     print("Largest =", b)
# else:
#     print("Largest =", c)

#     #PRINT FUNCTION

# print("harshitha pulluri")

# ##sub
# a = 10
# b = 20
# result = a - b
# print("Subtraction:", result)

# ##syntax of func
# def greet():
#     print("Hello, welcome to Python")
# greet()

# ##Function with Parameters
# def add(a, b):
#      sum = a + b
#      print("Sum:", sum)
# add(10, 20)

# ##Function with Return Value
# def multiply(a, b):
#  result = a * b
#  return result
# ans = multiply(5, 4)
# print("Multiplication:", ans)

# ##Function for Subtraction
# def subtraction(a, b):
#   result = a - b
#   print("Subtraction:", result)
# subtraction(20, 10)

# ##Simple square Program

# def square(n):
#     return n * n
# num = 6
# print("Square:", square(num))

# ##simples cubes
# def cube(n):
#     return n * n * n
# number = 4
# print("Cube:", cube(number))

# ##perfect number

# num = int(input("Enter a number: "))
# sum_val = 0
# for i in range(1, num):
#     if num % i == 0:
#         sum_val += i
# if sum_val == num:
#     print("Perfect Number")
# else:
#    print("Not Perfect Number")


# int(input("Enter a number: "))
# sum_val = 0
# for i in range(1, num):
#     if num % i == 6:
#         sum_val += i
# if sum_val == num:
#      print("Perfect Number")
# else:
#     print("Perfect Number")

    
# ch = input("Enter a character: ")
# if ch in "aeiouAEIOU":
#      print("Vowel")
# else:
#       print("Consonants")

# #squares
# def square(n):
#     return n * n
# num = 12
# print("Square:", square(num))

# list1 = ["burger", "phone", "teacher","hardware","doctor"]
# list2 = ["coke", "charger", "student","software","patient"]
# join_list = []
# for i in range(len(list1)):
#     join_list.append(list1[i])
#     join_list.append(list2[i])
# print(join_list) 

from ast import List


numbers = [10, 20, 30, 40, 50]
print(numbers)
#Append
numbers.append(60)
print(numbers)
#Remove
numbers.remove(30)
print(numbers)
#Update
numbers[1] = 25
print(numbers)

def twoSum(nums, target):
    d = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in d:
            return [d[diff], i]
        d[nums[i]] = i
# Sample Input
nums = [1, 5, 10, 15]
target = 100
# Function Call
print(twoSum(nums, target))


# class Solution(object):
#     def twoSum(self, nums, target):
#         hashmap = {}
#         for i in range(len(nums)):
#             complement = target - nums[i]
#             if complement in hashmap:
#                 return [hashmap[complement], i]
#             hashmap[nums[i]] = i

#EXAMPLE
# class Event:
#   count=0
#   def __init__(self,name,city):
#        self.name = name
#        self.city = city
#   def increment(self):
#       Event.count+= 1
#   def display(self):
#       print(Event.count)
# while(True):
#     print("1.Reg \n 2. Count \n 3.Exit")
#     choice = int(input("Enter your choice: "))
#     if choice == 1:
#         name = input("enter your name: ")
#         city = input("enter your city:")
#         e1=Event(name,city)
#         e1.increment()
#     elif choice==2:
#         e1.display()
#     else:
#         exit()

#created me
# class Bank:
#     count=0
#     def __init__(self,customername,balanceamount):
#          self.name = customername
#          self.city = balanceamount
#     def increment(self):
#          Bank.count+= 1
#     def decrement(self):
#          Bank.count-= 1
#     def display(self):
#         print("count=",Bank.count)
# e1=None
# while(True):
#      print("0.depoist \n 1.withdrawl \n 2.Exit")
#      choice = int(input("Enter your choice: "))
#      if choice == 0:
#         customername = input("enter the customername:")
#         balanceamount = input("enter your balanceamount:")
#         e1=Bank(customername,balanceamount)
#         e1.increment()
#      elif choice==1:
#        if e1 is not None:
#         e1.decrement()
#         e1.display()
    
#      elif choice == 2:
#          break
#      else:
#           print("invalid choice")

# class Bank:
#     def __init__(self, name, balance=0.0):
#         self.name = name
#         self.balance = balance
#     def deposit(self, amount):
#         self.balance += amount
#         print("Available balance:", self.balance)
#     def withdraw(self, amount):
#         if self.balance >= amount:
#             self.balance -= amount
#             print("Withdrawal successful.")
#         else:
#             print("Not enough money.")
#         print("Available balance:", self.balance)
# print("Welcome to Bank")
# name = input("Enter your name: ")
# balance = float(input("Enter your balance: "))
# b1 = Bank(name, balance)
# while True:
#     print("\nChoose an option")
#     print("w - Withdraw")
#     print("d - Deposit")
#     print("e - Exit")
#     ch = input("Enter your choice: ")
#     if ch == "w":
#         amount = float(input("Enter amount to withdraw: "))
#         b1.withdraw(amount)
#     elif ch == "d":
#         amount = float(input("Enter amount to deposit: "))
#         b1.deposit(amount)
#     elif ch == "e":
#         print("Thank you for using the bank.")
#         break
#     else:
#         print("Invalid choice. Please try again.")

# class Employee:
#     total=0
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def reg_sal(self,sal):
#         self.total=(sal*12)-(sal*12*0.1)
#         print(self.total)

#     def wag_sal(self,wag):
#         self.total=wag*30
#         print(self.total)

# name=input("enter your name")      
# age=int(input("enter your age"))  
# print("1.reg \n2.wage")    
# ch = int(input("enter your choice"))
# e1=Employee(name,age)
# if(ch==1):
#     e1.reg_sal(30000)
# elif(ch==2):
#     e1.wag_sal(500)

#calculate even numbers maximum no.of subarrays with size "k"
# arr = list(map(int, input("Enter array elements: ").split()))
# k = int(input("Enter k: "))
# count = 0
# sum = 0
# for i in range(k):
#     if arr[i] % 2 == 0:
#         count += 1
#         sum = sum+arr[i]
# print(count)
# for i in range(k, len(arr)):
#     if arr[i - k] % 2 == 0:
#         sum = sum-arr[i-k]
#         count -= 1
#     if arr[i] % 2 == 0:
#         sum = sum+arr[i]
#         count += 1
#     print(count)

# s = input("Enter a string: ")
# vowels = 0
# consonants = 0
# for ch in s:
#     if ch.isalpha():
#         if ch.lower() in "aeiou":
#             vowels += 1
#         else:
#             consonants += 1
# print("Vowels =", vowels)
# print("Consonants =", consonants)

#TO ACCEPT STRING FROM THE USER MAX COUNT OF CONSONSNATS SLIDING WINDOW TECHNIQUES
#1ST WAY
# s = input("Enter string: ")
# k = int(input("Enter k: "))
# vowels = "aeiou"
# count = 0
# for i in range(k):
#     if s[i].isalpha() and s[i] not in vowels:
#         count += 1
# maxcount = count
# for i in range(k, len(s)):
#     if s[i - k].isalpha() and s[i - k] not in vowels:
#         count -= 1
# if s[i].isalpha() and s[i] not in vowels:
#         count += 1
# if count > maxcount:
#         maxcount = count
# print("Maximum consonants in a window of size", k, "=", maxcount)

#2ND WAY
# s=input("enter")
# k=int(input("enter a string"))
# c=0
# for i in range(k):
#      if s[i] not in "aeiou":
#           c+=1
# maxi=c
# for i in range(k,len(s)):
#      if s[i] not in "aeiou":
#           c-=1
#      maxi=max(maxi,c)
# print(maxi)

#linear
# def Linear(nums,sele):
#      for i in range(len(nums)):
#           if sele==nums[i]:
#                return i
#           return -1
# nums=list(map(int,input("enter:").split()))
# sele=int(input("enter:"))
# print(Linear(nums,sele))

#BINARY
# def Binary(nums,sele):
#      left=0
#      right=len(nums)-1
#      while left<=right:
#           mid=(left+right)//2
#           if nums[mid]==sele:
#                return mid
#           elif nums[mid]>sele:
#                right=mid-1
#           else:
#                left=mid+1
#      return -1
# nums=list(map(int,input("enter:").split()))
# sele=int(input("enter:"))
# print(Binary(nums,sele))
