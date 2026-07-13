# def appu():   #creating a function
#     print("i am appu")
# def bunty():
#     appu()    #calling a function inside another function
#     print("i am bunty")
# def chintu():
#     bunty()
#     print("i am chintu")
# chintu()

# def adding(a,b):  #creating a function with parameters
#     c=a+b
#     print(c)
# adding(10,20)   #calling a function with arguments
# adding("python","programming")
# n1=int(input("enter num1"))
# n2=int(input("enter num2"))
# adding(n1,n2)

# def total_marks(external,internal):
#     total = external + internal
#     print("Total marks:",total)
# total_marks(30,40)   #passing both values to the function
# total_marks(40,10)   #passing both values to the function

# def mul(a,b):
#     print(a*b)
# mul(10,20)
# mul(20,10)      #positional arguments
# mul(b=15,a=20)   #passing values in different order using keyword arguments

def fun1():
    return "hello"
print(fun1())   #function returning a value
res = fun1()   # result storing the return value in a variable
print(res)

#returing multiple values from a function
def func1(a,b):
    c = a+b
    d = a-b
    return c,d
res = func1(10,20)
print(res)
res1,res2 = func1(30,40)   #unpacking the returned values into separate variables
print("res1:",res1)
print("res2:",res2) 
