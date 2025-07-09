"""
-----------------------
[Project Description: ]
-----------------------

Here's a mini project for you:

Password Validator System

Create a password validation system that checks multiple criteria and provides feedback using conditional expressions, string methods, and logical operators.

Requirements:

Check if password length is at least 8 characters
Check if password contains both uppercase and lowercase letters
Check if password contains at least one digit
Check if password doesn't contain spaces
Provide overall validation status and specific feedback
Your Task: Write conditional expressions to:

Determine if each criterion is met
Provide an overall "VALID" or "INVALID" status
Give specific feedback messages
Variables to use:

Variables to use:
password = "MyPass123"
username = "john_doe

Hints:

Use .islower(), .isupper(), .isdigit() string methods
Use len() function
Use in operator to check for spaces
Use and, or, not logical operators
Combine multiple conditions in your conditional expressions
Try to create at least 5 different conditional expressions that validate different aspects of the password!

"""

password = "MyPass12"
username = "john_doe"
lowercase_check = "MyPass12"
uppercase_check = "MyPass12"
check_digit = "MyPass12"
check_space = "My Pass 12"

#STRING METHODS
password = len(password)
print(password)
lowercase_check = lowercase_check.islower()
print(lowercase_check)
uppercase_check = uppercase_check.isupper()
print(uppercase_check)
check_digit = check_digit.isdigit()
print(check_digit)
check_space = check_space.isspace()
print(check_space)


#CONDITIONAL EXPRESSIONS

criteria = "VALID" if password == 8 else "INVALID"
print(criteria)
criteria = "VALID" if lowercase_check else "INVALID"
print(criteria)
criteria = "VALID" if uppercase_check else "INVALID"
print(criteria)
criteria = "VALID" if check_digit else "INVALID"
print(criteria)
criteria = "VALID" if check_space else "INVALID"
print(criteria)