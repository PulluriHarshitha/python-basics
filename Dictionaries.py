thisdict = {
  "name": "harshu",
  "age": "20",
  "year": 2005
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

bike["country"] = "england"

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

  



