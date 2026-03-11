#without functions repetitive code

temp1 = 55
celsius1 = (temp1 - 32)*5/9
print (celsius1)

temp2 = 65
celsius2 = (temp2 - 32)* 5/9
print(celsius2)

#with functions-reusable code

def farhenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32 ) * 5/9
print(farhenheit_to_celsius(55))
print(farhenheit_to_celsius(65))