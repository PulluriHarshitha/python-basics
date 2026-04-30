ch = input("Enter a character: ")
if ch in "aeiouAEIOU":
     print("Vowel")
else:
     print("Consonant")

# #palindrome num
num = int(input("Enter a number: "))
temp = num
rev = 0
while num > 0:
     digit = num % 10
     rev = rev * 10 + digit
num = num // 10
if temp == rev:
     print("Palindrome number")
else:
    print("Not a palindrome")

##palindrome string
text = input("Enter a string: ")
if text == text[::-1]:
     print("Palindrome string")
else:
     print("Not a palindrome")

# #prime number
num = int(input("Enter a number: "))
flag = 0
if num > 1:
     for i in range(2, num):
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
 
##largest of three numbers
# a = int(input())
# b = int(input())
# c = int(input())
# largest = max(a, b, c)
# print("Largest:", largest)

##days in a week
days = ["Monday", "Tuesday", "Wednesday", "Thursday",
         "Friday", "Saturday", "Sunday"]
for day in days:
     print(day)

 #months in a year
months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]
for month in months:
#     print(month)
  
##to display month name using number
month = int(input("Enter month number: "))
months = ["January", "February", "March", "April", "May", "June",
           "July", "August", "September", "October", "November", "December"]
if 1 <= month <= 12:
     print("Month is:", months[month - 1])
else:
     print("Invalid input")


# #find the largest of three numbers
a = int(input())
b = int(input())
c = int(input())
if a >= b and a >= c:
     print(a)
elif b >= c:
     print(b)
else:
     print(c)

#simple prime number
n = int(input())
flag = True
if n <= 1:
    flag = False
else:
     for i in range(2, n):
        if n % i == 0:
            flag = False
            break
if num:
     print("Prime")
else:
     print("Not Prime")
 
##swapping of two nums
a = int(input())
b = int(input())
a, b = b, a
print(a, b)

name = input("Enter your name: ")
print("Hello", name)
for i in range(1, 6):
     print(i)



##fibonacci series
n = int(input("Enter number of terms: "))
# a, b = 0, 1
print("Fibonacci Series:")
for i in range(n):
 print(a, end=" ")
     #a, b = b, a + b


##recursive fibonacci program
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
n = int(input("Enter number of terms: "))
print("Fibonacci Series:")
for i in range(n):
     print(fibonacci(i), end=" ")


##fiboonaci series vth loop method
def fibonacci(n):
 for _ in range(n):
   print(a, end=" ")

a, b = b, a + b
n = int(input("Enter number of terms: "))
 #fibonacci(n)

 #lists
list = [10, 20, 30, 40]
print("Max:", max(list))
print("Min:", min(list))


 #number guessing game
import random
num = random.randint(1, 10)
guess = int(input("Guess number (1-10): "))
if guess == num:
    print("Correct!")
else:
     print("Wrong! Number was:", num)

#file handling
with open("data.txt", "w") as f:
   f.write("Python streak day 9")
with open("data.txt", "r") as f:
   print(f.read())

#dictionary example
student = {"name": "Harshitha", "age": 18, "course": "Python"}
print(student["name"])

#simple calculator
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Add =", a + b)
print("Sub =", a - b)
print("Mul =", a * b)
print("Div =", a / b)

#print numbers from 1 to 10
for i in range(1, 11):
    print(i)
 

 #simple interest
p = int(input("Enter principal: "))
t = int(input("Enter time: "))
r = int(input("Enter rate: "))
si = (p * t * r) / 100
print("Simple Interest =", si) 

#Area of Circle
r = float(input("Enter radius: "))
area = 3.14 * r * r
print("Area =", area)

#Print Even Numbers from 1 to 20
for i in range(2, 21, 2):
    print(i)

    #Find Square and Cube
n = int(input("Enter number: "))
print("Square =", n*n)
print("Cube =", n*n*n) 

#Print Table of a Number
n = int(input("Enter number: "))
for i in range(1, 11):
    print(n, "x", i, "=", n*i)

#area of a circle
r = float(input("Enter radius: "))
area = 3.14 * r * r
print("Area =", area)  


#DICTIONARY EXAMPLES
student = {
    "name": "Harshitha",
    "age": 18,
    "course": "Python"
}
print(student["name"])
print(student["age"])

#Find Duplicate Elements in List
lst = [1, 2, 3, 4, 2, 5, 3, 6 ,10]
duplicates = []
for i in lst:
    if lst.count(i) > 1 and i not in duplicates:
        duplicates.append(i)
print("Duplicates:", duplicates)


#example
x = int(1)
y = int(2.8)
z = int("3")
print(x)
print(y)
print(z)

#string
name ="harshu"
print(name)
print(type(name))

#range
n = int(input("Enter number of terms: "))
a = 0
b = 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

#Program to Find GCD of Two Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
while b != 0:
    temp = b
    b = a % b
    a = temp
print("GCD is:", a)


#Sort a List
numbers = []
n = int(input("Enter number of elements: "))
for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)
numbers.sort()
print("Sorted list:", numbers)

#count to vowels to string
string = input("Enter a string: ")
count = 0
for char in string:
    if char.lower() in "aeiou":
        count += 1
print("Number of vowels:", count)


#Find 2nd Largest Number in a List
numbers = [10,30,45,78,20]
numbers.sort()
print("Second largest number:", numbers[-2])

#Check Palindrome String
text = input("Enter a string: ")
if text == text[::-1]:
    print("Palindrome string")
else:
    print("Not a palindrome")

#Remove Duplicates from List
numbers = [1, 2, 2, 3, 4, 4, 5]
unique = list(set(numbers))
print("List without duplicates:", unique)

#EXAMPLE
print("hello world")

#mar 17
n = int(input("Enter number of terms: "))
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

#palindrome check
text = input("Enter a string: ")
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

#simple calculator 
def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    return a / b
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("1.Add 2.Sub 3.Mul 4.Div")
choice = int(input("Enter choice: "))
if choice == 1:
    print(add(a, b))
elif choice == 2:
    print(sub(a, b))
elif choice == 3:
    print(mul(a, b))
elif choice == 4:
    print(div(a, b))
else:
    print("Invalid choice")

#number guessing game
import random
number = random.randint(1, 100)
while True:
    guess = int(input("Guess number (1-100): "))
    if guess > number:
        print("Too high")
    elif guess < number:
        print("Too low")
    else:
        print("Correct!")
        break

#matrix addition
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

result = [[0, 0], [0, 0]]

for i in range(2):
    for j in range(2):
        result[i][j] = A[i][j] + B[i][j]

print("Result:")
for row in result:
    print(row)

#matrix subtract 
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

result = [[0, 0], [0, 0]]

for i in range(2):
    for j in range(2):
        result[i][j] = A[i][j] - B[i][j]

print("Result:")
for row in result:
    print(row)

#file operation 
# Write
f = open("sample.txt", "w")
f.write("Hello Python")
f.close()
# Reads
f = open("sample.txt", "r")
print(f.read())
f.close()

#matrix addition
A = [[1, 5], [3, 7]]
B = [[5, 6], [7, 6]]
result = [[0, 0], [0, 0]]
for i in range(2):
    for j in range(2):
        result[i][j] = A[i][j] + B[i][j]

a = 10
b = 20
sum = a + b
print("Sum:", sum)


a = 100
b = 200
sum = a + b
print("Sum:", sum)

a = 45
b = 55
sum = a - b
print("diff:",)




