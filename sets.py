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
del thisset  #it should total del,it shows error

        #LOOP SETS
        
thisset = {"backbenchers", "dearkavya", "surya"}
for x in thisset:
    print(x)

      #JOIN SETS
    #UNION

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)  #union() method returns a new set with all items from both sets.

set1 = {"a","b","c"}  
set2 = {1,2,3}  
set3 = set1 | set2
print(set3)   # "|" instead use name operator
  
set1 = {"a","b","c"}
set2 = {1,2,3}
set3 = {"harshu","chachu"}
set4 = {"srinivas","kalyani"}
myset = set1.union(set2,set3,set4)
print(myset)   #joining multiple sets by using union

set1 = {"a","b","c"}
set2 = {1,2,3}
set3 = {"harshu","chachu"}
set4 = {"srinivas","kalyani"}
myset = set1 | set2 | set3 | set4
print(myset)  #by using union operator

x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)
print(z)  #union methods allow join set with other datatypes like list,tuples

  #UPDATE

Set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)    #update method insert all items from one to another set

   #INTERSECTION

set1 = {"google", "infosys", "tcs","techmahindra"}
set2 = {"google", "microsoft", "IBM","tcs"}
set3 = set1.intersection(set2)  #intersection will return a new set it keeps a duplicate elements
print(set3)

et1 = {"google", "infosys", "tcs","techmahindra"}
set2 = {"google", "microsoft", "IBM","tcs"}
set3 = set1 & set2  #intersection using a operator
print(set3)

set1 = {"apple", "IBM", "TCS","oracle"}
set2 = {"google", "microsoft", "apple","wipro","TCS"}
set1.intersection_update(set2)
print(set1)  #intersection_update() removes everything except the common elements and updates the original set.


set1 = {"apple", 1,  "deloite", 0, "IBM"}
set2 = {False, "google", 1, "apple", 2, True, "IBM"}
set3 = set1.intersection(set2)
print(set3)  #values True and 1 are considered the same value. The same goes for False and 0.


    #DIFFERENCE