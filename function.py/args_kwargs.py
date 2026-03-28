def my_function(*kids):
  print("The youngest child is " + kids[1])
my_function("harshu", "sweetie", "kanamma")


#accessing indiviual arguments example1
def my_function(*args):
  print("Type:", type(args))
  print("First argument:", args[0])
  print("Second argument:", args[1])
  print("Third argument:", args[2])
  print("All arguments:", args)
my_function("harshu","sweetie","ammu")

#accessing indiviual arguments example2
def my_function(*args):
  print("Type:", type(args))
  print("First argument:", args[0])
  print("Second argument:", args[1])
  print("Third argument:", args[2])
  print("All arguments:", args)
my_function("hasini","sahasra","chachu")

#Using *args with Regular Arguments
def my_function(greeting, *names):
  for name in names:
    print(greeting, name)

my_function("Hello", "harshitha", "hasini")

#A function that calculates the sum of any number of values:
def my_function(*numbers):
  total = 0
  for num in numbers:
    total += num
  return total
print(my_function(1, 2, 3))
print(my_function(10, 20, 30, 40))
print(my_function(5))

def my_function(*numbers):
  total = 0
  for num in numbers:
    total += num
  return total
print(my_function(5,6,7,8,9,10))
print(my_function(50,60,70,80,90,100))
print(my_function(17))
