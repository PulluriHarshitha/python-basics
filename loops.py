#range(start,end,step)
# for i in range(2,5):
#     print(i) # Output: 2, 3, 4
# for i in range(-5,-1):
#     print(i) 
# for i in range(4,-1,-1):
#     print(i) 
# for j in range(3,30,3):
#     print(j)
# for i in range(3):
#     print(i) # Output: 0, 1, 2
    

# i = 0
# while i < 5:
#     print(i)
#     if(i ==4):
#         break
#     i+=1

# n=int(input("ENTER A NUMBER: ")) #-123
# org=n  #original=-123
# if(n<0):
#     n=n*-1 #123
# rev=0
# while(n!=0):
#     dig =n %10
#     rev=rev*10 +dig
#     n=n//10
# if(org < 0):
#     print("Reversed num", rev*-1)
# else:
#     print("Reversed num",rev)


#5! ---->5*4*3*2*1  FACTORIAL OF NUMBER
n = int(input())
fact = 1
for i in range(1,n+1):
    fact = fact*i #fact = 1*1=1, fact=1*2=2, fact=2*3=6, fact=6*4=24, fact=24*5=120
print("Factorial", fact)

#ARMSTRONG NUMBERs:is anumber that is equal to the sum of cubes of its digits. each digit is raised to the power of total number of digits.For example, 153 is an armstrong number because 1^3 + 5^3 + 3^3 = 153

n = int(input())
n_dup= n #153
org = n #org = 153
c = len(str(n)) #c = 3
sumD = 0
while(n!=0):
    dig = n%10 #3,5,1
    sumD += dig**c  #153
    n=n//10 #0
if(org == sumD):
    print("Armstrong number")
else:
    print("Not an armstrong number")
