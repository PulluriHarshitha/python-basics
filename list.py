#creation of list

mylist = ["apple","banana","cherry"]
print(mylist)  

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)   #allow duplicate values only

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(len(thislist))   #length of list

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(list1)
print(list2)
print(list3)   #list datatypes(int,str,bool)

list1 = ["harshu", 20, True, "female"]  #allows list in all datatypes
print(list1)

mylist = ["apple", "banana", "cherry"]
print(type(mylist))   #define the class using type

#ACCESS THE LIST ITEMS

thislist = ["apple", "banana", "cherry"]
print(thislist[2])
thislist = ["apple", "banana", "cherry"]
print(thislist[-3])  #negative indexing(starts from last)
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])  # -1 is excluded

#CHANGE LIST ITEMS

thislist = ["c","python","java"]
thislist[2] = "c++"
print(thislist)

thislist = ["c","c++","java","python","dsa"]
thislist[1:4] = "html","css","javascript"
print(thislist)

thislist = ["c","c++","java","ml"]
thislist.insert(4,"python")
print(thislist)

#APPEND ITEMS

thislist = ["java", "c++", "html"]
thislist.append("python")
print(thislist)

thislist = ["java","c++","python","ML"]
thislist.insert(2,"java script")
print(thislist)

thislist1 = ["java","python","c++","DS"]
thislist2 = ["html","css","c#","reactjs"]
thislist1.extend(thislist2)
print(thislist1)

thislist = ["java", "python", "atcd"]
thistuple = ("html", "css","javascript")
thislist.extend(thistuple)
print(thislist)   #Add elements of a tuple to a list

#REMOVE SPECIFIED ITEM A LIST

thislist = ["rose", "jasmine", "tulips"]
thislist.remove("rose")
print(thislist)

thislist = ["tulips" , "rose", "jasmine", "sunflower", "lily", "lotus"]
thislist.remove("lotus")
print(thislist)  #remove a element in first occurence
