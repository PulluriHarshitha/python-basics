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


marks = 75
if marks >= 35:
    if marks >= 75:
        print("Distinction")
    else:
        print("Pass")
else:
    print("Fail")



score = 25
attendance = 90
submitted = True
if score >= 60:
  if attendance >= 80:
    if submitted:
      print("Pass with good standing")
    else:
      print("Pass but missing assignment")
  else:
    print("Pass but low attendance")
else:
  print("Fail")


score = 82
extra_credit = 5
if score >= 90:
  if extra_credit > 0:
    print("A+ grade")
  else:
    print("A grade")
elif score >= 80:
  print("B grade")
else:
  print("C grade or below")
