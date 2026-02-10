# ch = input("Enter a character: ")
# if ch in "aeiouAEIOU":
#     print("Vowel")
# else:
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

#house price prediction
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
# Sample data
data = {
    'Area': [800, 1000, 1200, 1500, 1800],
    'Price': [40, 50, 60, 75, 90]
}
df = pd.DataFrame(data)
X = df[['Area']]
y = df['Price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = LinearRegression()
model.fit(X_train, y_train)
# Prediction
print(model.predict([[1600]]))


#even or odd prediction

from sklearn.tree import DecisionTreeClassifier
X = [[1], [2], [3], [4], [5], [6]]
y = [1, 0, 1, 0, 1, 0]  # 1 = Odd, 0 = Even
model = DecisionTreeClassifier()
model.fit(X, y)
print(model.predict([[10]]))  # Even -> 0
print(model.predict([[7]]))   # Odd -> 1


#student marks prediction

import numpy as np
from sklearn.linear_model import LinearRegression
hours = np.array([[1], [2], [3], [4], [5]])
marks = np.array([35, 45, 55, 65, 75])
model = LinearRegression()
model.fit(hours, marks)
print("Predicted marks for 6 hours:", model.predict([[6]])[0])
