ch = input("Enter a character: ")
if ch in "aeiouAEIOU":
    print("Vowel")
else:
    print("Consonant")

    #palindrome num
num = int(input("Enter a number: "))
temp = num
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
if temp == rev:
    print("Palindrome number")
else:
    print("Not a palindrome")

#palindrome string
text = input("Enter a string: ")
if text == text[::-1]:
    print("Palindrome string")
else:
    print("Not a palindrome")

#prime number
num = int(input("Enter a number: "))
flag = 0
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            flag = 1
            break
        if flag == 0:
         print("Prime number")
    else:
        print("Not a prime number")
else:
    print("Not a prime number")

#armstrong num
num = int(input("Enter a number: "))
temp = num
sum = 0
while num > 0:
    digit = num % 10
    sum = sum + digit**3
    num = num // 10
if temp == sum:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
