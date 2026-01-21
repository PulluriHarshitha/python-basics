#PLANE SQUARE
n = 4
for i in range(n):
    for j in range(n):
        print("#", end=" ")
    print()

#NUMBER SQUARE
n = 5
for i in range(1, n + 1):
    for j in range(n):
        print(i, end=" ")
    print()

#SAME NUMBER IN ALL ROWS
n = 4
for i in range(n):
    for j in range(1, n + 1):
        print(j, end=" ")
    print()

#HOLLOW SQUARE
n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


#same alphabets in eachrow
i = 0
while i < 4:
    j = 0
    while j <= i:
        print(chr(65 + i), end=" ")
        j += 1
    print()
    i += 1


#square with increasing alphabets
n = 4
for i in range(n):
    for j in range(n):
        print(chr(65 + i), end=" ")
    print()


#square with continous alphabets
n = 5   #same rows & cols
ch = 65
for i in range(n):
    for j in range(n):
        print(chr(ch), end=" ")
        ch += 1
    print()