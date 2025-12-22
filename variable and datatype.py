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

x = int(1)     #specify a variable type dataset[int]
y = int(2.8)    
z = int(3)     
print(x)
print(y)
print(z) 

a = float(1)     #specify a variable  type in dataset [float]
b = float(2.8)
c = float(3)
d = float(4.2)
print(a)
print(b)
print(c)
print(d)

x = str("friendsship")  #specify a variable type in dataset [string]
y = str("rohith")
z = str("harshu")
print(x)
print(y)
print(z)

a= 15
print(type(a))

b=14.6
print(b)

a= ("harshitha")
print(len(a))

marks = [8]
print(len(marks))   

a = True
print((a))

list = [1,2,3,4,5,6]
print("list of numbers:",list)

tuple =(10,20,30,40,50)
print(tuple[1])

student = {
    "name": "Harshitha",  #dictionary
    "age": 20,
    "course": "Python"
}
print(student)


student = {
    "name": "Harshitha",
    "age": 22,
    "course": "python"
}

for key in student.keys():
    print(key)


   