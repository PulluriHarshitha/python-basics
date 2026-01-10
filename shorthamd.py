#syntax : value_if_true if condition else value_if_false

#simple example
a = 50
b = 30
print("a is greater") if a > b else print("b is greater")

#assigning a value
age = 18
status = "Adult" if age >= 18 else "Minor"
print(status)

#even or odd
num = 6
result = "Even" if num % 2 == 0 else "Odd"
print(result)

#without else
a = 5
if a > 3: 
    print("Greater than 3")

#multiple conditions on one line
a = 339
b = 338
print("A") if a > b else print("=") if a == b else print("B")

#examples
x = 2004
y = 2005
min_value = x if x > y else y
print("Minimum value:", min_value)