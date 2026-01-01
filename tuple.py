thistuple = ("apple", "banana", "cherry")
print(thistuple)

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)   #allow duplicates on tuple

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))  #length of tuple

thistuple = ("apple",)
print(type(thistuple))
thistuple = ("apple")
print(type(thistuple))  #tuple indicates with comma at last 

tuple1 = ("JULY", "DEC", "JUN")
tuple2 = (6,25,28)
tuple3 = (True, False, False)
print(tuple1)
print(tuple2)
print(tuple3)    #tuple items can be of any data type

tuple1 = ("Harshu", 19, True,  "female")
print(tuple1)   #tuple can contain different data types

thistuple = tuple(("sun", "mon", "sat"))  # note the double round-brackets as constructor
print(thistuple)

#ACCESS TUPLE ITEMS

thistuple = ("JAN", "FEB", "MAR")
print(thistuple[1])

thistuple = ("JUL", "JUN", "AUG")
print(thistuple[-1])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

thistuple = ("JAN", "FEB", "MAR", "APR", "JUN", "JUL", "AUG")
print(thistuple[2:5])

 #UPDATE TUPLES

x = ("JAN", "FEB", "MAR")
y = list(x)
y[1] = "DEC"
x = tuple(y)
print(x)   #Convert the tuple into a list

thistuple = ("JAN", "FEB", "MAR")
y = list(thistuple)
y.append("APR")
thistuple = tuple(y)  #Convert the tuple into a list, add "APR", and convert it back into a tuple
print(thistuple)

thistuple = ("JAN", "FEB", "MAR")
y = ("DEC",)
thistuple += y
print(thistuple)

thistuple = ("MAR", "JUN", "JUL")
y = list(thistuple)
y.remove("JUN")
thistuple = tuple(y)
print(thistuple)   #REMOVE LIST

thistuple = ("JULY", "DEC", "JUNE")
print(thistuple)
del thistuple   #del the tuple

#UNPACK TUPLES

thistuple = ("sunday", "monday", "friday")
a, b, c = thistuple
print(a)
print(b)
print(c)   #means assigning each value of a tuple to separate variables in one statement

fruits = ("soap", "shampoo", "paste")
(santoor, chick, closeup) = fruits
print(santoor)
print(chick)
print(closeup)

week = ("sunday", "monday", "thursday", "friday")
a, b, *c = week
print(a)
print(b)
print(c)   #If there are more values than variables, you can use * before a variable will collect all extra values into a list

student = ("Harshitha", 21, "IT")
name, _, branch = student
print(name)
print(branch)   #_ means “ignore this value”













