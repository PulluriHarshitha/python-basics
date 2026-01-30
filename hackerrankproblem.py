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
