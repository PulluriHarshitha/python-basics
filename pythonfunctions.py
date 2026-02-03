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

#arbitary arguments

def myFun(*args, **kwargs):
    print("Non-Keyword Arguments (*args):")
    for arg in args:
        print(arg)
    print("\\nKeyword Arguments (**kwargs):")
    for key, value in kwargs.items():
        print(f"{key} == {value}")
myFun('Hey', 'Welcome', first='pulluri', mid='harshu', last='sweetie') 

#function within function

def f1():
    s = 'I LOVE YOU ROHITH'
    def f2():
        print(s)

    f2()
f1()

#anomymous function

def cube(x): return x*x*x   # without lambda
cube_l = lambda x : x*x*x  # with lambda
print(cube(6))
print(cube_l(22))

#return statement in function

def square_value(num):
    return num**2
print(square_value(31))
print(square_value(50))

#pass by value & pass by reference
#Mutable objects: Changes inside the function affect the original object.
#Immutable objects: The original value remains unchanged.

# Function modifies the first element of list
def myFun(x):
    x[3] = 20
list = [10, 11, 12 ,13]
myFun(list)
print(list)   # list is modified
# Function tries to modify an integer
def myFun2(x):
    x = 20
a = 13
myFun2(a)
print(a)     # integer is not modified
#based on index values the o/p should br print