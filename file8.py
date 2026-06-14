#if statements = do something if a condition is true else do something different if the condition is false

age = int(input("Enter your age:"))

if age > 150:
    print("You are a vampire!\nyou cannot vote!!")
elif age >= 18:
    print("You can vote!\nYou are an adult.")
elif age == 0:
    print("You are not born yet!")
else:
    print("You cannot vote!\nYou are a minor.")