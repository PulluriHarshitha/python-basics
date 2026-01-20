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


#number triangle
for i in range(1, 5):
    for j in range(1, i + 1):   #number triangle
        print(j, end=" ")
    print()


#sample number triangle
for i in range(1, 5):
    for j in range(i):
        print(i, end=" ")   #same num triangle
    print()


#inverted triangle
for i in range(4, 0, -1):   #inverted triangle
    for j in range(i):
        print("*", end=" ")
    print()


#pyramid pattern
n = 4
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(i):
        print("* ", end="")   #pyramid pattern
    print()


#alphabet pattern
for i in range(4):
    for j in range(i + 1):
        print(chr(65 + j), end=" ")    #alphabet pattern
    print()


#diamond pattern
    n = 4
# Upper part
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(i):
        print("* ", end="")
    print()
# Lower part
for i in range(n - 1, 0, -1):
    print(" " * (n - i), end="")
    for j in range(i):
        print("* ", end="")
    print()


#hollow square pattern
n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#hollow triangle
n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j == 1 or j == i or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


#number pyramid
n = 4
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


#mixed patterns
for i in range(1, 6):
    for j in range(i):
        if i % 2 == 0:
            print("*", end=" ")
        else:
            print(i, end=" ")
    print()

#floyds triangle
num = 1
for i in range(1, 5):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()


#butterfly pattern
n = 3
# Upper part
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print(" " * (2 * (n - i) * 2), end="")
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

# Lower part
for i in range(n - 1, 0, -1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print(" " * (2 * (n - i) * 2), end="")
    for j in range(1, i + 1):
        print("*", end=" ")
    print()


#alphabet pattern
n = 3
ch = 65
# Upper part
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(i):
        print(chr(ch + i - 1), end=" ")
    print()
# Lower part
for i in range(n - 1, 0, -1):
    print(" " * (n - i), end="")
    for j in range(i):
        print(chr(ch + i - 1), end=" ")
    print()



#hollow pyaramid
n = 5
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1 or i == n:
            print("*", end="")
        else:
            print(" ", end="")
    print()
