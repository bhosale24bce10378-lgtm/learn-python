#Matlibs game
#A word game where you create a story by filling in the blanks with different types of words (nouns, verbs, adjectives, etc.)

print("Welcome to the Matlibs game!")
print("Please fill in the blanks with the appropriate words to create your own story.")


adjective1 = input("enter an adjective(descriptive):")
noun1 = input("enter a noun(person, place, or thing):")
adjective2 = input("enter another adjective(descriptive):")
place1 = input("enter a place(home):")
verb1 = input("Enter a verb ending with 'ing' (action word):")
place2 = input("Enter a place(outside):")
adjective3 = input("Enter another adjective(descriptive):")
noun2 = input("Enter another noun(person, place, or thing):")

print(f"Once upon a time, there was a {adjective1} {noun1} who lived in a {adjective2} {place1}.")
print(f"She loved {verb1} in the {place2}.")
print(f"One day, she met a {adjective3} {noun2} who was also {verb1} in the {place2}.")
print(f"They became friends and lived happily ever after in the {place1}.")
print("The end.")