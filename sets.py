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

          #ADD SET ITEMS

thisset = {"vishwa", "bala", "sundari"}
thisset.add("justmarried")
print(thisset)   #add one item to a set use the add() method.

a = {"softwaredeveloper","surya", "schoolmates"}
b = {"justmarried", "dearkavya","telugumedium"}
a.update(b)
print(a)   #update() is used to add elements of one set into another set.


thisset = {"justmarried", "dearkavya", "schoolmates"}
mylist = ["surya", "telugumedium"]
thisset.update(mylist)
print(thisset)      #Add Any Iterable if list,set,tuple

     #REMOVE SET ITEMS

thisset = {"justmarried", "dearkavya", "telugumedium"}
thisset.discard("dearkavya")
print(thisset)    #remove an item in a set, use the remove(), or the discard() method.

hisset = {"justmarried", "dearkavya", "telugumedium"}
thisset.remove("telugumedium")
print(thisset)


thisset = {"justmarried", "dearkavya", "surya"}
x = thisset.pop()
print(x)        #removed item
print(thisset)   #print(thisset) #the set after removal


thisset = {"justmarried", "surya", "schoolmates"}
thisset.clear()
print(thisset)   #The clear() method empties the set


thisset = {"merizindagithu", "terebin", "sher"}
del thisset
print(thisset)  #it should total del,it shows error






