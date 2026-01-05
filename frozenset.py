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
print(fs)  #Frozenset = printed paper, Copy = another printout of the same paper
print(cp)  #We usually don’t need to copy a frozenset because it is immutable, but copy() exists for consistency and to support generic code.

a = frozenset({1, 2, 3, 4})
b = frozenset({3, 4,})
print(a.difference(b))
print(a - b)        #“Remove common values from a, keep only unique values of a.”

a = frozenset({1, 2})
b = frozenset({3, 4})
c = frozenset({2, 3})
print(a.isdisjoint(b))
print(a.isdisjoint(c))   #No common = True ,Common exists = False

a = frozenset({1, 2})
b = frozenset({1, 2, 3})
print(a.issubset(b))
print(a <= b)
print(a < b)  #a is completely inside b, and b has extra values — so all checks return True

