#Variables store data in memory and scope defines the specific region of a program where a variable is accessible. It dictates the visibility and lifetime of the variable within the source code. Variables are categorized into two primary scopes: Global and Local.
#Local Variable: Local variables are defined inside a function and exist only during its execution. They cannot be accessed from outside the function.

def greet():
    msg = "Hello from inside the function!"
    print(msg)
greet()