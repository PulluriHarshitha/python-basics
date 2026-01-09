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
