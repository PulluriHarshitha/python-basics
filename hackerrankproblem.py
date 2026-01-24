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
