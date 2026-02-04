 #ABSTRACT() function
# An integer
var = 3150
print('Absolute value of integer is:', abs(var))

#floating point number
float_number = -1234
print('Absolute value of float is:',abs(float_number))

#abs() a complex number

complex_number = (3 - 5j)
print('Absolute value or Magnitude of complex is:', abs(complex_number))


#time-distance calculation using py.abs() function
#Distance  = Speed * Time
#Time = Distance / Speed
#Speed = Distance / Time
#above formulaes used in prgm

# Function to calculate speed
def cal_speed(dist, time):
    print(" Distance(km) :", dist)
    print(" Time(hr) :", time)
    return dist / time
# Function to calculate distance traveled
def cal_dis(speed, time):
    print(" Time(hr) :", time)
    print(" Speed(km / hr) :", speed)
    return speed * time
# Function to calculate time taken
def cal_time(dist, speed):
    print(" Distance(km) :", dist)
    print(" Speed(km / hr) :", speed)
    return dist / speed
# Driver Code
# Calling function cal_speed()
print(" The calculated Speed(km / hr) is :",
      cal_speed(abs(56), abs(5)))
print("")
# Calling function cal_dis()
print(" The calculated Distance(km) :",
      cal_dis(abs(62), abs(-2)))
print("")
# Calling function cal_time()
print(" The calculated Time(hr) :",
      cal_time(abs(48), abs(4.5)))

# B.BUILT-IN-FUNCTIONS

var = -25
print('Absolute value of integer is:', abs(var))

#MAXIMUM OF THREE NUMBERS

var1 = 10
var2 = 20
var3 = 30
largest = max(var1,var2,var3)
print(largest)

#minimum of list

list1 = 10
list2 = 20
list3 = 30
smallest = min(list1,list2,list3)
print(smallest)