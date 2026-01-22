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

#contionous num rectangle
rows = 8
cols = 16
num = 1
for i in range(rows):
    for j in range(cols):
        print(num, end=" ")
        num += 1
    print()

    #hollow rectangle in numbers
rows = 5
cols = 10
for i in range(rows):
    for j in range(cols):
        if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
            print(6, end=" ")
        else:
            print(" ", end=" ")
    print()


#same rectangle alphabets 
rows = 5
cols = 10
for i in range(rows):
    for j in range(cols):
        print("A", end=" ")
    print()


#row wise alphabet rectangle
rows = 5
cols = 10
for i in range(rows):
    for j in range(cols):
        print(chr(65 + i), end = " ")
    print()

#colwise alphabet rectangle
rows = 5
cols = 10
for i in range(rows):
    for j in range(cols):
        print(chr(65 + j), end = " ")
    print()

    #continous alphabets rectangle
rows = 5
cols = 10
ch = 65
for i in range(rows):
    for j in range(cols):
        print(chr(ch), end=" ")
        ch += 1
    print()

#hollow rectangle with alphabets
rows = 5
cols = 10
for i in range(rows):
    for j in range(cols):
        if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
            print("H", end=" ")
        else:
            print(" ", end=" ")
    print()
