
'''
🔧 Mini Project: Custom Username & Age Calculator
📝 Description:
Create a program that:

Asks the user for their first name and last name.

Asks the user for their birth year.

Calculates the user’s age.

Generates a username by combining their name and age.

Example Output:

What is your first name? John  
What is your last name? Doe  
What year were you born? 2002  
Hello, John Doe! You are 23 years old.  
Your username is: johndoe23


'''

firstname = input("What is your first name? ")
lastname = input("What is your last name? ")
birthyear = input("What year were you born? ")

birthyear = int(birthyear)

age = 2025 - birthyear #Fixed this to make the project functionable

username = firstname.lower() + lastname.lower() + str(age) #Was unsure so I checked this was my mistake

print(f"Hello, {firstname} {lastname}. You are {birthyear} years old.")
print(f"Your username is {username}.")


