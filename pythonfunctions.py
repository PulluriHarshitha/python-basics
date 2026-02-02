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