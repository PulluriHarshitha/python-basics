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
    a = int(input().strip())
    b = int(input().strip())
    
    print(a + b)      # Sum
    print(a - b)      # Difference  
    print(a * b)      # Product

#operators on division on above logic

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)

#task using square the numbers 

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i*i) 
        