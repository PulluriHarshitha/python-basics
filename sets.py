thisset = {"vishwa" , "sundari" ,"justmarried" }
print(thisset)   #the set list is unordered, meaning: the items will appear in a random order.

thisset = {"vishwa","sundari", "sundari", "justmarried", "vishwa"}
print(thisset)  #it doesnot allows duplicates

thisset = {"vishwa", "sundari", "justmarried", True, 1, 2}
print(thisset)  #The values True and 1 are considered the same value in sets, and are treated as duplicates

thisset = {"justmarried", "vishwa", "sundari", False, True, 0 }
print(thisset)  #The values False and 0 are considered the same value in sets, and are treated as duplicates


thisset = {"sundari", "vishwa"}
print(len(thisset))   #Length of a Set

set1 = {"vishwa", "sundari", "justmarried"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
print(set1)
print(set2)
print(set3)   #Set Items - Data Types

set1 = {"vishwa", 34, True, 40, "male"}
print(set1)  #different data types

a = 10
print(type(a))      # <class 'int'>
b = "hello"
print(type(b))      # <class 'str'>
c = [1, 2, 3]
print(type(c))      # <class 'list'>  type() is used to find the data type (class) of a variable.

thisset = set(("bala", "vishwa", "justmarried"))
print(thisset)  # constructor the set list is unordered, so the result will display the items in a random order.


   #ACCESS SET ITEMS 

thisset = {"vishwa", "bala", "justmarried"}
for x in thisset:
  print(x)   #set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.


thisset = {"vishwa", "bala", "justmarried"}
print("vishwa" in thisset)   #Check if "vishwa" is present in the set


thisset = {"vishwa", "sundari", "justmarried"}
print("vishwa" not in thisset)

