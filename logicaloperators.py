#and-Returns True if both statements are true
#or - Returns True if one of the statements is true
#not - Reverses the result, returns False if the result is true

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

a = 10
b = 5
print(a > 5 and  b < 5)   

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

a = 20
b = 33
c = 9
print (c > a or a > b)

a = 330
b = 200
print(not a > b)

a = 10
print(not a > 5)
print(not a < 5)


age = 20
if age >= 18 and age <= 60:
    print("Eligible")  #using if operator


username = "admin"
password = "1234"
if username == "harshu" and password == "1234":
    print("Login Successful")
else:
    print("Login Failed")

score = 31
if score >= 0 and score <= 100:
  print("Valid score")
else:
  print("Invalid score")

 