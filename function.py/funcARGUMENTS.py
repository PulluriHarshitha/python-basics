def my_function(fname):
    print(fname + "reddy")

my_function("rohith")
my_function("harshitha")


#FUNCTIONS v/s ARGUMENTS
#From a function's perspective:
#A parameter is the variable listed inside the parentheses in the function definition.
#An argument is the actual value that is sent to the function when it is called.

def my_function(name):  #name is parameter
    print("hello", name)
my_function("HARSHITHA") #harshitha is an argument 

#number of arguments

def my_function(fname, lname):
    print(fname + " " +lname)
my_function("PULLURI" ,"HARSHITHA") 