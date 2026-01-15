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
