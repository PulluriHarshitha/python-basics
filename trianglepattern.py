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


#Right-Angle Alphabet Triangle
n = 5
for i in range(n):
    for j in range(i + 1):
         print(chr(65 + i), end = " ")
    print()

 # Alphabet Increasing Triangle 
  
n = 5
for i in range(n):
    for j in range(i + 1):
        print(chr(65 + j), end=" ")
    print()

#Continuous Alphabet Triangle

n = 7
ch = 65
for i in range(1, n + 1):
    for j in range(i):
        print(chr(ch), end=" ")
        ch += 1
    print()

#Inverted Number Triangle

n = 5
for i in range(n, 0, -1):
    for j in range(i):
        print(i, end=" ")
    print()

#inverted alphabet triangle
n = 5
for i in range(n,0,-1):
    for j in range(i):
        print(chr(65 + i), end = " ")
    print()

#INVERTED # TRIANGLE 
n = 5
for i in range(n, 0, -1):
    for j in range(i):
        print("#", end=" ")
    print()