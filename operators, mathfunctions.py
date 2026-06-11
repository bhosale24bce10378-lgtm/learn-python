#operators

friends = 0

#Addition
#friends = friends + 1
friends += 1
print(friends)

#Subtraction
#friends = friends - 5
friends -= 5
print(friends)

#Multiplication
#friends = friends * -3
friends *= -3
print(friends)

#Division 
#friends = friends / 3
friends /= 3
print(friends)

#Exponents
#power
#friends = friends ** 2
friends **= 2
print(friends)

#Modulus
#remainder
remainder = friends % 3
print(remainder)


#Math functions

x = 3.14
y = -4
z = 5

#round(x) = rounds x to the nearest integer
result = round(x)
print(result)

#abs(y) = distance of y from 0 on the number line
result = abs(y)
print(result)

#pow(z, 2) = z raised to the power of 2
result = pow(z, 2)
print(result)

#max(x, y, z) = returns the largest value among x, y, and z
result = max(x, y, z)
print(result)

#min(x, y, z) = returns the smallest value among x, y, and z
result = min(x, y, z)
print(result)


##importing math module for more math functions
import math

x1 = 9.9

#value of pi
print(math.pi)

#value of e
print(math.e)

#math.sqrt(x1) = returns the square root of x1
result = math.sqrt(x1)
print(result)

#math.ceil(x1) = rounds x1 up to the nearest integer
result = math.ceil(x1)  
print(result)

#math.floor(x1) = rounds x1 down to the nearest integer
result = math.floor(x1)
print(result)

#math.factorial(z) = returns the factorial of z
result = math.factorial(z) #Factorial is not defined for negative numbers or non-integers
print(result)

#math.log(z) = returns the natural logarithm of z
result = math.log(z) #Logarithm is not defined for non-positive numbers
print(result)

#math.sin(x1) = returns the sine of x1 (x1 is in radians)
result = math.sin(x1)  #Sine is defined for all real numbers, but the result will be between -1 and 1
print(result)

#math.tan(z) = returns the tangent of z (z is in radians)
result = math.tan(z)
print(result)