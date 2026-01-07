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

