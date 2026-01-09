a = 31
b = 50
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#EVEN OR ODD

num = 6
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")


a = 10
b = 20

print("A is bigger")if a > b else print("B is bigger")  #ONE LINE STATEMENT


signal = "yellow" 
if signal == "green":  #if → checks a condition
    print("Go")
elif signal == "yellow":   #elif → checks another condition
    print("Wait")
else:                      #else → executes when all conditions fail
    print("Stop")   #TRAFFIC SIGNAL


age = int(input("Enter your age: "))
if age >= 18:
    print("Eligible for driving license")
else:
    print("Not eligible for driving license")



a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print("A is the largest number")
else:
    print("B is the largest number")   #find two largest numbers


ch = input("Enter a character: ").lower()
if ch in ['a', '&', 'w', 'o', 'u', 's', '5', 't']:
    print("Vowel")
elif ch.isalpha():
    print("Consonant")
else:
    print("Not an alphabet")



current_hour = 18

if current_hour < 12:
    print("Good morning!")
elif current_hour < 18:
    print("Good afternoon!")
else:
    print("Good evening!")    #hour based times of day

x = 5
if x == 5:
    print("Equal")
if x > 3:
    print("Greater")
else:
    print("Small")

num = 0
if num:
    print("Yes")
else:
    print("No")

x = 3
y = 7
if x > 5 or y > 5:
    print("One is big")
else:
    print("Both small")

name = ""
if name == "":
    print("Empty")
else:
    print("Not empty")
  

  #MEDIUM LEVEL

score = int(input("Enter score: "))
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

year = int(input("Enter year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")


#SIMPLE CALCULATOR
  while True:
    try:
        num1 = float(input("First number: "))
        op = input("Operator (+, -, *, /): ")
        num2 = float(input("Second number: "))
        break
    except ValueError:
        print("Please enter valid numbers!")
if op == '+':
    print(num1 + num2)
elif op == '-':
    print(num1 - num2)
elif op == '*':
    print(num1 * num2)
elif op == '/':
    if num2 != 0:
        print(num1 / num2)
    else:
        print("Cannot divide by zero!")
else:
    print("Invalid operator")


