#SYNTAX
#while condition:
    #statements

i = 0
while i <= 5:
    print(i)
    i+= 1  

a = 0
while (a < 6):
    a = a + 1
    print("Harshu")

i = 1
while i < 6:
  print(i)
  if (i == 3):
    break
  i += 1

  n = 9
for i in range(0, n):
    print(i)

li = ["harshu"]
for index in range(len(li)):
    print(li[index])

    i = 0
while i < 6:
  i += 1
  if i == 5:
    continue
  print(i)

for i in range(1, 5):
    for j in range(i):
        print(i, end=' ')   #right angled triangle
    print()

rows = 4
cols = 6

for i in range(rows):
    for j in range(cols):
        print("*", end=" ")   #stars
    print()
 
rows = 4
cols = 6

for i in range(rows):
    for j in range(cols):   #rectangle numbers
        print(1, end=" ")
    print()

rows = 4
cols = 5

for i in range(1, rows+1):   #rectangle row vth nums
    for j in range(cols): 
        print(i, end=" ")
    print()

rows = 4
cols = 5

for i in range(rows):
    for j in range(1, cols+1):    #rectangle col with nums
        print(j, end=" ")
    print()

# Example: Searching for an element in a list

a = [1, 3, 5, 7, 9, 11]
val = 9
for i in a:
    if i == val:
        print(f"Found at {i}!")
        break
else:
    print(f"not found")

for letter in 'harshitha':
    pass
print('last Letter :', letter)

name = "harshitha"
print("3rd letter:", name[2])   #using indexing


#number increment triangle

for i in range(1, 7):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

for i in range(1, 7):
    for j in range(i):
        print("#", end=" ")
    print()