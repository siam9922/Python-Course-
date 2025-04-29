#Variable = A container for a value (string, integer, float, boolean etc.)
# A variable behaves like a box that can hold a value.


#String Variables
# A string is a sequence of characters enclosed in quotes (single or double).
# Strings can contain letters, numbers, symbols, and spaces.

first_name = "Siam Hasan" 
print(first_name) # This will print the value of the variable first_name

print(f"Hello my name is {first_name}") # This will print the value of the variable first_name in a formatted string

email = "siamhasan773@gmail.com"
print(f"Your email is {email}") # This will print the value of the variable email in a formatted string

food = "Chicken Nuggets" # This is a string variable
print(f"I love {food}") # This will print the value of the variable food in a formatted string
ice_cream = "chocolate"
print(f"{ice_cream}, is a good favour")

#Integer Variables
# An integer is a whole number (positive or negative) without a decimal point.
# Integers can be used for counting, indexing, and performing arithmetic operations.
age = 25

quantity = 10
print(f"You are {age} years old")
print(f"You are buying {quantity} pens for school")

num_of_students = 30
print(f" There are {num_of_students} in the class")


#Float 
# Decimal values 

gpa = 3.2
price = 17.99
distance = 20


print(f"This medicine is {price} dollars ")
print(f"My gpa is: {gpa}")
print(f"The mall is {distance} km away")

#Boolean 
#True/false

is_he_a_student = True
for_sale = False 
is_online = True 


if for_sale:
    print("This car is for sale")
else:
    print("This car is not for salecle")


#print(f"Is he a student? {is_he_a_student}")

if is_he_a_student:
    print("You are a student") 
else:
    print ("You are not a student")


if is_online:
    print("Yes he is")
else: 
    print("No he is not")