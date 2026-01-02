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