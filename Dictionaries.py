thisdict = {
  "name": "harshu",
  "age": "20",
  "year": 2006
}
print(thisdict)  #Create and print a dictionary

thisdict = {
  "name": "harshu",
  "city": "hyderabad",
  "year": 2025
}
print(thisdict["city"])   #the "city" value of the dictionary

thisperson = {
  "name": "harshu",
  "city": "Mumbai",
  "year": 2005,
  "year": 2025,
  "name": "rohitreddy"
}
print(thisdict)   #Dictionaries cannot have two items with the same key


thisdict = {
    "name": "Harshitha",
    "age": 20,
    "course": "Python"
}
print(len(thisdict))   #len of dictionary

thisdict = {
  "name": "harshitha",
  "year": 2005,
  "college": "SMEC",
  "colors": ["black", "white", "blue"],
  "topics" : "True"
}
print(thisdict)     #different datatypes allow single dictionaries

#ACCESS ITEM DICTIONARIES

thisdict = {
  "name": "harshu",
  "age": "20",
  "year": 2005
}
x = thisdict["name"]
print(x)     #creates a dictionary and stores the value of the key "name" into the variable x.

thisdict =	{
  "name": "harshu",
  "age": "20",
  "year": 2005
}
x = thisdict.get("year")
print(x)       #used to get() method


#GET KEYS
thisdict = {
  "name": "harshu",
  "age": "20",
  "year": 2005
}
x = thisdict.keys()
print(x)     #gets all the keys from the dictionary and prints them


#GET KEYS UPDATED PGM
bike = {
"brand": "royal enfield",
"model": "Classic 500 ",
"year": 1901
}

x = bike.keys()

print(x) #before the change

bike["country"] = "england"  #keys are always immutable object,values are mutable or immutable

print(x) #after the updated keys after pgm



#GET VALUES

bike = {
  "brand": "royal enfield",
  "model": "GT-650",
  "year": 1963
}
x = bike.values()
print(x)     


#GET key values updated

bike = {
"brand": "royal enfield",
"model": "GT-650 ",
"year": 1963
}

x = bike.values()
print(x) #before the change
bike["country"] = "england"
print(x)


#GET ITEMS

car = {
  "brand": "BMW",
  "model": "BMW iX3",
  "year": 2025
}
x = car.items()
print(x)  


#UPDATED A CAR ITEMS

car = {
"brand": "BMW",
"model": "BMW iX3",
"year": 2024
}
x = car.items()
print(x) #before the change
car["engine"] =  "Petrol" 
print(x) #after the change

#ADD A NEW ELEMENT

car = {
"brand": "BMW",
"model": "BMW iX3",
"year": 2024
}
x = car.items()
print(x) #before the change
car["engine"] =  "Petrol" 
car["color"] = "grey"
print(x)

#CHECK IF KEYS EXISTS OR NOT

car = {
"brand": "BMW",
"model": "BMW iX3",
"year": 2024
}
if "model" in car:
  print("Yes, 'model' is one of the keys in the car dictionary")


      #CHANGE DICTIONARY ITEMS

  thisdict =	{
  "brand": "Pulsar",
  "model": "ns2",
  "year": 1989
}
thisdict["year"] = 2018
print(thisdict)   #change the value of a specific item 

thisdict = {
  "brand": "pulsar",
  "model": "ns25",
  "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict)    #update the dict

      #ADD DICT ITEMS

thisdict =	{
  "brand": "GT-650",
  "model": "RX54",
  "year": 1998
}
thisdict["color"] = "WHITE"
print(thisdict)   #Adding the items

      #REMOVE A ITEMS

thisdict = {
  "brand": "GT-650",
  "model": "XMP4",
  "year": 1998
}
thisdict.pop("model")
print(thisdict)   #pop() method removes a item with specified name

thisdict = {
  "brand": "GT-650",
  "model": "XMP4",
  "year": 1998
}
thisdict.popitem()
print(thisdict)    #popitem() method removes the last inserted item

thisdict = {
  "name" : "harshu",
  "age"  : "20",
  "dept" : "IT"
  }
del thisdict["age"]
print(thisdict)   #del keyword removes the item with specified key name

thisdict = {
  "brand": "GT-650",
  "model": "XMP4",
  "year": 1998
}
thisdict.clear()
print(thisdict) #clear() methods empties the dictS

      #LOOP DICTIONARIES
      
thisdict = {
  "name" : "harshu",
  "age"  : "20",
  "dept" : "IT"
  }
for x in thisdict:
  print(thisdict[x])   #Print all key names in the dictionary, one by one

thisdict = {
  "name" : "harshu",
  "age"  : "20",
  "dept" : "IT"
  }
for x in thisdict:
  print(thisdict[x])  #Print all values in the dictionary, one by one

thisdict = {
  "name" : "harshu",
  "age"  : "20",
  "dept" : "IT"
  }
for x in thisdict.values():
  print(x)   #the values() method to return values of a dictionary

thisdict = {
  "name" : "harshu",
  "age"  : "20",
  "dept" : "IT"
  }
for x in thisdict.keys():
  print(x)   #the keys() method to return the keys of a dictionary
  
thisdict = {
  "name" : "harshu",
  "age"  : "20",
  "dept" : "IT"
  }
for x, y in thisdict.items():
  print(x, y)  #Loop through both keys and values, by using the items() method
 
 
             #COPY DICTIONARIES
thisdict = {
  "NAME": "Harshitha",
  "DEPT": "IT",
  "CLG": "SMEC",
  "PLACE" : "Dhulapalli"
}
mydict = thisdict.copy()
print(mydict)   #copy of a dictionary with the copy() method

hisdict = {
  "NAME": "Harshitha",
  "DEPT": "IT",
  "CLG": "SMEC",
  "PLACE" : "Dhulapalli"
}
mydict = dict(thisdict)
print(mydict) #  Another way to make a copy is to use the built-in function dict().

  #NESTED DICTIONARIES

student = {                 #main dict
    "id": 1250,
    "name": "Harshitha",
    "marks": {             #key value another dict
        "ATCD": 85,       # dict inside dict(nested dict)
        "ADA": 90,
        "ES": 88,
        "DM" : 87,
    }
}
print("Student ID:", student["id"])    #to nested access the dict
print("Student Name:", student["name"])
print("ATCD Marks:", student["marks"]["ATCD"])
print("ADA Marks:", student["marks"]["ADA"])
print("ES Marks:", student["marks"]["ES"])
print("DM:", student["marks"]["DM"])


#EXAMPLE 1 OF NESTED DICTIONARIES

student1 = {    # Create three dictionaries
    "name": "Harshitha",
    "age": 20,
    "course": "Python"
}
student2 = {
    "name": "Rohith",
    "age": 21,
    "course": "Java"
}
student3 = {
    "name": "Harith",
    "age": 22,
    "course": "Data Science"
}
students = {
    "student1": student1,
    "student2": student2,
    "student3": student3
}   # Create one dictionary containing all three dictionaries
print(students)    #Print the nested dictionary

#EXAMPLE 2

Engineering = {
"student1" : {                   
    "name": "Harshitha",
    "age": 20,
    "course": "Python"
},
"student2" : {
    "name": "Rohith",
    "age": 21,
    "course": "Java"
},
"student3" : {
    "name": "Harith",
    "age": 22,
    "course": "Data Science"
}
}
for x, obj in Engineering.items():   #it gives key and value
  print(x)                            #student key 1,2,3
  for y in obj:                        #student detail dict
    print(y + ':', obj[y])               #prints student name ,age,key

# players = {}
# n = int(input("Enter number of players: "))
# for i in range(n):
#     name = input("Enter player name: ")
#     score = int(input("Enter score: "))
#     players[name] = score
# total = sum(players.values())
# average = total / len(players)

# print("\nPlayers and Scores:")
# for name, score in players.items():
#     print(name, ":", score)

# print("Total Score:", total)
# print("Average Score:", average)

#2
# n = int(input("enter no of players:"))
# d1={}
# for i in range(n):
#     name=(input("enter your name:"))
#     score=int(input("enter your score:"))
#     d1[name]=score
# print(d1)
# s=0
# for i in d1:
#     s=s+d1[i]
# print(s)
# avg = s/n
# print(avg)

#3 max number
# n = int(input("enter no of players:"))
# d1={}
# for i in range(n):
#     name=(input("enter your name:"))
#     score=int(input("enter your score:"))
#     d1[name]=score
# print(d1)
# maxi = max(d1.values())
# for i in d1.keys():
#    if d1[i]==maxi:
#       print(i,d1[i])

#4 frequency of letters
# s1 = input("enter a string:")
# d1 = {}
# for i in s1:
#   if i in d1:
#     d1[i]+=1
#   else:
#     d1[i]=1
# print(d1)

#classes and objects
# class Student:
#   name = " "
#   rollno = " "
#   dept = " "
#   def accept(self):
#     self.name="harshitha"
#     self.rollno="23K81A1250"
#     self.dept="IT"
#   def disp(self):  #usages 2
#     print(self.name)
#     print(self.rollno)
#     print(self.dept)
# s1=Student()
# s1.accept()
# s1.disp()

#2 def accept(self):
#     self.name=input()
#     self.rollno=input()
#     self.dept=input()

#3 def accept(self,n,r,d):
  #   self.name=n
  #   self.rollno=r
  #   self.dept=d
  # def disp(self):  #usages 2
  #   print(self.name)
  #   print(self.rollno)
  #   print(self.dept)
#   s1=Student()
# s1.accept("a",9,"cse")
# s1.disp()
# s2=Student()
# s2.accept("b",8,"cse")
# s2.disp()
