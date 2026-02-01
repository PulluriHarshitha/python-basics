#ifelse hackerrank
import sys
if __name__ == '__main__':  
 n = int(input().strip())
if n % 2 != 0:   #input 3(odd)
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:  #input 24 (even<20)
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")

#operators hackerank

if __name__ == '__main__':
    a = int(input("Enter a first number"))
    b = int(input("Enter a second number"))
    
    print(a + b)      # Sum
    print(a - b)      # Difference  
    print(a * b)      # Product

#operators on division on above logic

if __name__ == '__main__':
    a = int(input("Enter a first number"))
    b = int(input("Enter a second number"))
    print(a//b)
    print(a/b)

#task using square the numbers 

if __name__ == '__main__':
    n = int(input("enter a number"))
    for i in range(n):
        print(i*i) 

    #leapyear

def is_leap(year):
     if year % 400 == 0:
        return True
     if year % 100 == 0:
        return False
     if year % 4 == 0:
        return True
     return False

     return leap

year = int(input("enter a year"))
print(is_leap(year))

#print a function

if __name__ == '__main__':
    n = int(input("Enter a number"))
for i in range(1, n + 1):
    print(i, end='')

#list comprehension

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
result = [[i, j, k]
          for i in range(x + 1)
          for j in range(y + 1)
          for k in range(z + 1)
          if i + j + k != n]
print(result)

#reverse array

if __name__ == '__main__':
    n = int(input())
arr = list(map(int, input().split()))
unique_scores = sorted(set(arr), reverse=True)
runner_up = unique_scores[1]
print(runner_up)

#list
if __name__ == '__main__':
    N = int(input("ENTER A NUM"))
    list = []
    for _ in range(N):
        command = input().split()
        op = command[0]
        if op == "insert":
            i = int(command[1])
            e = int(command[2])
            list.insert(i, e)
        elif op == "print":
            print(list)
        elif op == "remove":
            e = int(command[1])
            list.remove(e)
        elif op == "append":
            e = int(command[1])
            list.append(e)
        elif op == "sort":
            list.sort()
        elif op == "pop":
            list.pop()
        elif op == "reverse":
            list.reverse()

