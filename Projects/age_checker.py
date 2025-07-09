'''

🧪 Age and Name Checker Challenge
Instructions:

Ask the user for their name.

Ask the user for their age (as a number).

Based on the age, print:

"You're a child." if age < 13

"You're a teenager." if age is between 13 to 19

"You're an adult." if age is between 20 to 59

"You're a senior." if age is 60 or more

Bonus: If the name is "Alice" (case-sensitive), also print: "Hey Alice, welcome back!"


'''

name = input("What is your name? ")
alice = "Alice"
age = int(input("What is your age? "))


if name == "Alice":                      
    print(f"Hello Alice! Welcome back")
elif age < 13:
    print("You're a child.")
elif age <= 19:
    print("You're a teenager.")
elif age <= 59:
    print("You're an adult")
else:
    print("You're a senior.")
