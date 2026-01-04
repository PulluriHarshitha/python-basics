#CREATING A FROZEN SET

x = frozenset({"apple", "banana", "cherry"})
#display x:
print(x)
#display the data type of x:
print(type(x)) 
   
   #FROZENSET METHODS

   #COPY METHOD
   
fs = frozenset({1, 2, 3})
cp = fs.copy()
print(fs) #Frozenset = printed paper, Copy = another printout of the same paper
print(cp)  #We usually don’t need to copy a frozenset because it is immutable, but copy() exists for consistency and to support generic code.

