x = 5
y = "HARSHITHA"
print(x)
print(y)

x = 4       
x = "harshitha" 
print(x)

x = str(3)
y = int(3)
z = float(3)

print(x)
print(y)
print(z)

myvar = "HARSHITHA"
print(myvar)

myVariableName = "harshitha"   #camel case,except the first,starts with capital letter
MyVariableName = "harshitha"  #pascal case,every word starts with capital letter
my_variable_name = "harshitha" #snake case ,words are seperated by underscores

x, y, z = "Orange", "Banana", "Cherry"

print(x)
print(y)
print(z)  #many values to multiple varibales

x = y = z = "Orange"
print(x)
print(y)
print(z)  #one value to multiple variables

x = 5
y = 10
print(x + y)     #addition of two variables


x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is " + x)
myfunc()
print("Python is " + x)        #local variable inside function has higher precedence than global variable



def myfunc():
  global x
  x = "harshitha"
myfunc()
print(" this girl is " + x)


x = "Hello World"
print(x)

print(type("string"))     #data type of string

x = 20
print(x)

print(type("int"))        #data type of variable


x = ["apple", "banana", "cherry"]
print(x)

print(type("X")) 



x = 1        #int
y = 2.8       #float
z = 1j       #complex

print(type(x))
print(type(y))
print(type(z))   #python numbers

x = 1
y = 35656222554887711
z = -3255522
print(type(x))
print(type(y))
print(type(z))  #int can be of any unlimited length

x = 1.44
y = 7.656222554887711
z = -3.3255522
print(type(x))
print(type(y))
print(type(z))     #"floating point number" is a number, positive or negative, containing one or more decimals.

x = 35e3
y = 12E4
z = -87.7e100
print(type(x))
print(type(y))
print(type(z))
