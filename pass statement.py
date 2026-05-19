#The pass keyword in a function is used when we define a function but don't want to implement its logic immediately. 
#It allows the function to be syntactically valid, even though it doesn't perform any actions yet.

def fun():
    pass
fun() # Call the function

#In conditional statements
x = 50
if x <= 10:    #The else block runs only when the condition is False.
    pass     #placeholder for future logic
else:
    print (" x is 10 or less ")

x = 50
if x >= 10:
    pass
else:
    print ("x is 10 or less")


#IN LOOPS

for i in  range(10):
    if i == 5:
        pass   #do nothing stops
    else:
        print(i)


class EmptyClass:
    pass  # No methods or attributes yet
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        pass  # Placeholder for greet method
# Creating an instance of the class
p = Person("Emily", 30)

class EmptyClass:
    pass  # No methods or attributes yet


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
     print("hello" ,self.name)
     print("hello",self.age)
p = Person("emily", 20)
p.greet()