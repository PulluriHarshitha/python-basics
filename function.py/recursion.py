#Recursion means a function calling itself again and again to solve a problem in smaller parts.
#Instead of using loops, recursion breaks a big problem into smaller versions of the same problem.
#Basic Idea of Recursion
#Every recursive function has 2 parts:
#Base Case → condition to stop recursion
#Recursive Call → function calls itself
#Without a base case, the function runs forever and gives an error.


#SIMPLE STRUCTURE
def function_name():
    # Base case
    # Recursive call
    function_name()

    #EXAMPLE 1
def countdown(n):
    if n == 0:       #base case
        print("DONE")    
    else:
        print(n)
        countdown(n-1)    #recursive case
countdown(5)

    #EXAMPLE 2
def factorial(n):
    if n == 1:
        return 1
    else:
        return n *factorial(n-1)
print(factorial(10))

#EXAMPLE 3
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(3))

     #EXAMPLE 4
def sum_numbers(n):
    if n == 1:
        return 1
    return n + sum_numbers(n-1)
print(sum_numbers(4))

#EXAMPLE 5

def reverse_string(text):
    if len(text) == 0:
        return text
    return reverse_string(text[1:]) + text[0]
print(reverse_string("harshu"))