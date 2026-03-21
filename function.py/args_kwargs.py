def my_function(*kids):
  print("The youngest child is " + kids[1])
my_function("harshu", "sweetie", "kanamma")


#accessing indiviual arguments
def my_function(*args):
  print("Type:", type(args))
  print("First argument:", args[0])
  print("Second argument:", args[1])
  print("Third argument:", args[2])
  print("All arguments:", args)
my_function("harshu","sweetie","ammu")

#Using *args with Regular Arguments
def my_function(greeting, *names):
  for name in names:
    print(greeting, name)

my_function("Hello", "harshitha", "hasini")