#plane rectangle
rows = 5
cols = 10

for i in range(rows):
    for j in range(cols):
        print("*", end=" ")
    print()

#same number rectangle
rows = 5
cols = 10
for i in range(rows):
    for j in range(cols):
        print(1, end=" ")
    print()


#row different number rectangle
rows = 5
cols = 10
for i in range(1, rows+1):
    for j in range(cols):
        print(i, end=" ")
    print()


#col different number rectangle
rows = 5
cols = 10
for i in range(rows):
    for j in range(1,cols+1):
        print(j, end=" ")
    print()
