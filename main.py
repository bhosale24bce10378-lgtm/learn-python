#this is my 1st python code
# this is a comment

# This is a print statement
print("i love pizza")
print("this is good")

#Variables = A container for a value (strings, intergers, floats, booleans)
# A variable behaves as if it was the value that it contains

#Strings
first_name = "Veerashree"
print(first_name)
print(f"Hello {first_name}")

food = "pizza"
print(f"I love {food}")

email = "veerashree@example.com"
print(f"Your email is: {email}")

#integers
age = 20
print(f"You are {age} years old")

quantity = 3
print(f"you are buying {quantity} books")

people = 45
print(f"Your class has {people} students")

#floats
price = 10.99
print(f"The price of this is {price} cents")

temperature = 36.5
print(f"The temperature is {temperature} degrees Celsius")

gpa = 8.5
print(f"My gpa will be above {gpa}")

distance = 5.2
print(f"You ran {distance} km")

#booleans
is_student = True
print(f"Are you a student? {is_student}")

is_raining = False
print(f"is it raining? {is_raining}")

is_teacher = False

if is_teacher:
    print("you are a teacher")
else:
    print("you are not a teacher")

for_sale = True

if for_sale:
    print("this item is for sale")
else:
    print("this item is not for sale")

is_online = True
if is_online:
    print("user is online")
else:
    print("user is offline")

#Typecasting = converting a variable from one data type to another
# str(), int(), float(), bool()

name1 = "Veerashree"
age1 = 20
gpa1 = 7.3
is_student1 = True

print(f"The type of name1 = Veerashree is: {type(name1)}")
print(f"The type of age1 = 20 is: {type(age1)}")
print(f"The type of gpa1 = 7.3 is: {type(gpa1)}")
print(f"The type of is_student1 = True is: {type(is_student1)}")

gpa2 = int(gpa1)
print(f"The type of gpa2 = {gpa2} is: {type(gpa2)}")

age1 = str(age1)
print(f"The type of age1 = {age1} is: {type(age1)}")

age2 = 30
age2 += 10
print(f"If you are 30, you will be {age2} years old in 10 years")