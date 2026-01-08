#PYTHON IF STATEMENTS
a = 10
b = 5
print(a != b)  #not equal to 
print(a == b)  #equal to
print(a > b)  #greater than
print(a < b)  #less than
print(a <= b)   #lessthan or equal
print(a >= b)    #greater than or equal

age = 18
if age >= 18:
    print("You are eligible to vote")

number = 50
if number > 0:
  print("The number is positive")

x = 10
if x > 5:
    print("x is greater than 5")
    print("Condition is true")
    print("Value of x:", x)   #multiple satements inside one

  #ELIF KEYWORD

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
 
x = 20
if x > 0:
    print("Positive number")
elif x == 0:
    print("Zero")
else:
    print("Negative number")


age = 16
if age >= 18:
    print("Eligible to vote")
elif age >= 13:
    print("Teenager")
    print("Not eligible to vote")
else:
    print("Child")   #multiple statements elif

#weak cheacker

day = 6
if day == 1:
  print("Monday")
elif day == 2:
  print("Tuesday")
elif day == 3:
  print("Wednesday")
elif day == 4:
  print("Thursday")
elif day == 5:
  print("Friday")
elif day == 6:
  print("Saturday")
elif day == 7:
  print("Sunday")

#IF ELSE SYNTAX

#if condition:
    # code runs if condition is True
#else:
    # code runs if condition is False

marks = 65

if marks >= 90:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Grade C")


for i in range(5):
    print(i)
else:
    print("Loop finished")   #The else block executes after the loop completes normally (without break)


