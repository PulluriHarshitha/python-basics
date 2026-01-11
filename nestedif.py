#BASIC SYNTAX
#if outer_condition:
    #if inner_condition:
       # print("Both conditions met")

x = 11
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

num = 5
if num > 0:
    if num % 2 == 0:
        print("Positive and Even")
    else:
        print("Positive but Odd")
else:
    print("Negative number")

age = 16
has_license = True
if age >= 18:
  if has_license:
    print("You can drive")
else:
  print("You are too young to drive")
