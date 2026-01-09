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

