#right angle num triangle
n = 4
for i in range(1, n + 1):
    for j in range(i):    #outer loop -> rows [i]
        print(i, end=" ")  #innerloops -> cols
    print()
  