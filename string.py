a = "Hello"
print(a)     #printing a string

b = "Hello, World!"
print(b[3:5])    #slicing a string front

b = "Hello, World!"
print(b[2:])     #slicing a string back

a = "Hello, World!"
print(a.upper())    #converting to upper case

a = "Hello, World!"
print(a.lower())   #converting to lower case

a = " Hello, World! "
print(a.strip())    #removing whitespace

a = "Harshitha"
print(a.replace("H", "R"))  #replacing a string

a = "Harshitha,Rohith"
print(a.split(","))     #spliting a string to list 

a = "pulluri"
b = "harshitha"
c = a + b
print(c)           #merging two strings(concatenation)

a = "pulluri"
b = "harshitha"
c = a + " " + b
print(c)         #merging two strings with space in between

age = 20
txt = f"My name is Harshu, I am {age}"
print(txt)       #formatted string using number and name

price = 100
txt = f"The price is {price} rupees"
print(txt)    #formatted string using price

price = 100
txt = f"The price is {price:.2f} rupees"
print(txt)     #formated string using float with 2 decimal places :2f

txt = f"The price is {100 * 200} rupees"
print(txt)     #formatted string using expresssion inside math operators

 

