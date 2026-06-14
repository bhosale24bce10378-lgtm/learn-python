#finding the hypotenuse of a right angled triangle
import math
a = float(input("Enter the base of the triangle triangle:"))
b = float(input("Enter the height of the triangle:"))
hypotenuse = math.sqrt(a**2 + b**2)
print(f"The hypotenuse of right angled triangle with sides {a} and {b} is {round(hypotenuse, 2)}")