x = 31
y = 50          #ARTHAMETIC OPERATORS
print(x + y)  #addition
print(x - y)  #subtraction
print(x * y)  #multiplication
print(x / y)  #Division (returns a float)
print(x % y)  #modulus
print(x ** y)  #Exponentiation same as 31 power 50
print(x // y)  #It rounds DOWN to the nearest integer(floor division)

x = 50
y = 31             
#ASSIGNMENT OPERATORS 
   
#simple Assignment
print("x =", x) 
print("y =", y)
# Add and assign (x = x+y)
x += y
print(" x += y, x =", x)
# Subtract and assign (x = x-y)
x -= y
print(" x -= y, x =", x)
# Multiply and assign
x *= y
print(" x *= y, x =", x)
# Divide and assign
x /= y
print(" x /= y, x =", x)
# Modulus and assign
x %= y
print(" x %= y, x =", x)
# Floor division and assign
x //= y
print(" x //= y, x =", x)
# Power and assign
x **= y
print(" x **= y, x =", x)
# Bitwise AND assign(it works only with int,float)
x = int(x)  
x &= y
# Bitwise OR assign
x |= y
print(" x |= y, x =", x)
# Bitwise XOR assign
x ^= y
print(" x ^= y, x =", x)
# Right shift assign
x >>= y
print(" x >>= y, x =", x)
# Left shift assign
x <<= y
print(" x <<= y, x =", x)
# Walrus operator
print("Walrus operator:", (x := y))
print("Value of x after walrus:", x)


numbers = [1, 2, 3, 4, 5]
count = len(numbers)
if count > 3:
    print(f"List has {count} elements")

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")


x = 25
y = 6

print(x == y)  #equal to
print(x != y)  #not equal to
print(x > y)   #greater than
print(x < y)   #less than
print(x >= y)  #greaterthan or equal to
print(x <= y)  #lessthan or equal to

x = 5
print(1 < x < 10)  #chain comparsion
print(1 < x < 5)

#LOGICAL OPERATORS
x = 5     #Returns True if both statements are true
print(x > 3 and x < 10) 
print(x > 6 and x < 10)




