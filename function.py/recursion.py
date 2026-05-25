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

#EXAMPLE5 reverse string

def reverse_string(text):
    if len(text) == 0:
        return text
    return reverse_string(text[1:]) + text[0]
print(reverse_string("harshurohith"))

#example  6
def function(n):
    if n==4:
        return n
    else:
        return 2*function(n+1)
print(function(2))

#print 1 to n numbers
def print_numbers(n):
    if n == 0:
        return
    print_numbers(n - 1)
    print(n)
print_numbers(31)

#print n to 1 numbers
def print_reverse(n):
    if n == 0:
        return
    print(n)
    print_reverse(n - 1)
print_reverse(50)

#sum of n natural numbers
def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n - 1)
print(sum_n(8))

def sum_n(n):
    if n <= 0:
        return 0
    return n + sum_n(n - 2)
print(sum_n(5))

def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n - 1)
print(sum_n(5))


def palindrome(s):

#Types of Recursion
#Recursion can be broadly classified into two types: tail recursion and non-tail recursion. The main difference between them is related to what happens after recursive call.
#Tail Recursion: The recursive call is the last thing the function does, so nothing happens after it returns. Some languages can optimize this to work like a loop, saving memory.
#Non-Tail Recursion: The function does more work after the recursive call returns, so it can’t be optimized into a loop.