#right angle num triangle
n = 4
for i in range(1, n + 1):
    for j in range(i):    #outer loop -> rows [i]
        print(i, end=" ")  #innerloops -> cols
    print()
  
#increase the num in triangle
n = 6
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

#Continuous Number Triangle
n = 6
num = 1
for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()
