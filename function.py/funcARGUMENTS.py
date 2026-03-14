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

#DEFAULT parameter values
def my_function(name="friend"):
    print("hello" , name)
my_function("reethu")
my_function("shiny")
my_function("vaishu") 
my_function("rohith")
my_function()

#exmple2
def my_function(country = "Norway"):
  print("I am from", country)
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#mixed arguments
def my_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)

my_function("dog", name = "doggie", age = 7)

#Sending a list as an argument func()
def my_function(names):
  for name in names:
    print(name)
my_names = ["komaplly", "suchitra", "alwal"]
my_function(my_names)

