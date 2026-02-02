#call a function

def fun():
    print("Welcome to Function")
fun() 

#function parameters

def evenOdd(x):
    if (x % 2 == 0):
        return "Even"
    else:
        return "Odd"
print(evenOdd(16))
print(evenOdd(7))

#default arguments

def myFun(x, y=60):
    print("x: ", x)
    print("y: ", y)
myFun(30)

#keyword arguments
def student(fname, lname):
    print(fname, lname)
student(fname='harshu', lname='sweety')
student(lname='sweety', fname='harshu')

#positional keywords
def nameAge(name, age):
    print("Hi, I am", name)
    print("My age is ", age)
print("Case-1:")
nameAge("Harshu", 19)
print("Case-2:")
nameAge(19, "Harshu")