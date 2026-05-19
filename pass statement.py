#The pass keyword in a function is used when we define a function but don't want to implement its logic immediately. 
#It allows the function to be syntactically valid, even though it doesn't perform any actions yet.

def fun():
    pass
fun() # Call the function

#In conditional statements
x = 50
if x <= 10:    #The else block runs only when the condition is False.
    pass     #placeholder for future logic
else:
    print (" x is 10 or less ")
