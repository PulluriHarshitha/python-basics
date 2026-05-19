#Variables store data in memory and scope defines the specific region of a program where a variable is accessible. It dictates the visibility and lifetime of the variable within the source code. Variables are categorized into two primary scopes: Global and Local.
#Local Variable: Local variables are defined inside a function and exist only during its execution. They cannot be accessed from outside the function.

def greet():
    msg = "Hello from inside the function!"
    print(msg)
greet()

def greet():
    msg = "Hello!"
    print("Inside function:", msg)
greet()
print("Outside function:", msg)

#Global Variables:Global variables are declared outside all functions and can be accessed anywhere in the program, including inside functions.

msg = "Python is easy language"
def display():
    print("Inside function:", msg)
display()
print("Outside function:", msg)