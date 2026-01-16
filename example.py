#same alphabet in each row
i = 0
while i < 4:
    j = 0
    while j <= i:
        print(chr(65 + i), end=" ")
        j += 1
    print()
    i += 1

#inverted alphabet
i = 4
while i >= 1:
    j = 0
    while j < i:
        print(chr(65 + j), end=" ")
        j += 1
    print()
    i -= 1

#contionus alphabet
i = 1
ch = 65
while i <= 4:
    j = 1
    while j <= i:
        print(chr(ch), end=" ")
        ch += 1
        j += 1
    print()
    i += 1

#lowecase alphabets
i = 1
while i <= 4:
    j = 0
    while j < i:
        print(chr(97 + j), end=" ")
        j += 1
    print()
    i += 1

#same lowercase alphabets in eachrow
i = 0
while i < 4:
    j = 0
    while j <= i:
        print(chr(97 + i), end=" ")
        j += 1
    print()
    i += 1

#pattern using name letters
name = "HARSHITHA"
i = 1
while i <= 9:
    j = 0
    while j < i:
        print(name[j], end=" ")
        j += 1
    print()
    i += 1

#alphabet diamond pattern

i = 1
while i <= 3:
    space = 3 - i
    while space > 0:
        print(" ", end="")
        space -= 1

    j = 0
    while j < i:
        print(chr(65 + j), end=" ")
        j += 1
    print()
    i += 1

i = 2
while i >= 1:
    space = 3 - i
    while space > 0:
        print(" ", end="")
        space -= 1

    j = 0
    while j < i:
        print(chr(65 + j), end=" ")
        j += 1
    print()
    i -= 1

for i in range(4):
     for j in range(4):
        print("*", end=" ")    #square pattern
     print()
   
for i in range(1, 5):
    for j in range(i):    #right angled triangle
        print("*", end=" ")
    print()

for i in range(1, 5):
    for j in range(1, i + 1):   #number triangle
        print(j, end=" ")
    print()

for i in range(1, 5):
    for j in range(i):
        print(i, end=" ")   #same num triangle
    print()

for i in range(4, 0, -1):   #inverted triangle
    for j in range(i):
        print("*", end=" ")
    print()



