
#----------------------------------------------------------------------------------------------------------------------------------------------------

# Variable = A container for a value (string, integer, float, boolean etc.)
# A variable behaves like a box that can hold a value.

#----------------------------------------------------------------------------------------------------------------------------------------------------

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


#Re-watching course

#Use f-string to put in the code in the print statement

first_name = "Nathan"
last_name = "Drake"
food = "Mangos"
email = "jinho987@gmail.com"

print(f"Hello {first_name} {last_name}. Did you manage to find the chintamani stone yet?")
print(f"{food} are a great delecacy its filled with vitamins and a lot of natural sugars.")
print(f"Hey, {first_name} {last_name}. The email {email} has been hacked!")



#----------------------------------------------------------------------------------------------------------------------------------------------------



#Integer Variables
# An integer is a whole number (positive or negative) without a decimal point.
# Integers can be used for counting, indexing, and performing arithmetic operations.


age = 25

quantity = 10
print(f"You are {age} years old")
print(f"You are buying {quantity} pens for school")

num_of_students = 30
print(f" There are {num_of_students} in the class")



#Re-watching

#Integers
age = 25
quantities = 72
num_of_home_invadors = 46

print(f"Jidion your age is {age} years old")
print(f"Jidion stop buying {quantities} quantities of GTA 6 cds.")
print(f"Yesterday, the police arrested {num_of_home_invadors} number of home invadors in the state.")



#----------------------------------------------------------------------------------------------------------------------------------------------------



#Float Variables 
# A float (or floating-point number) is a number that has a decimal point.
# Floats can represent real numbers and are often used for calculations that require precision.
# Floats can be used for representing decimal values, such as prices, measurements, and scientific calculations.


gpa = 3.2
price = 17.99
distance = 20


print(f"This medicine is {price} dollars ")
print(f"My gpa is: {gpa}")
print(f"The mall is {distance} km away")


#Re-watching

price = 7.99
gpa = 1.5 
distance = 8.9 

print(f"George bought a box of cookies for ${price} but he was aressted for shoplifting.")
print(f"I almost failed math that would have dropped my gpa to {gpa}.")
print(f" I ran {distance}km to the beach for a lifeguard interview.")


#----------------------------------------------------------------------------------------------------------------------------------------------------


#Boolean Variables  
# A boolean variable can only have two values: True or False.
# It is often used to represent binary states or conditions.

is_he_a_student = True
for_sale = False 
is_online = True 


if for_sale:
    print("This car is for sale")
else:
    print("This car is not for sale")


#print(f"Is he a student? {is_he_a_student}")

if is_he_a_student:
    print("You are a student") 
else:
    print ("You are not a student")


if is_online:
    print("Yes he is")
else: 
    print("No he is not")


#re-watching course

is_student = False

if is_student:
    print("You are a student of the night!")
else:
    print("You are not the student")


is_for_sale = True

if is_for_sale:
    print("You are for sale")
else:
    print("You are not for sale")   



#----------------------------------------------------------------------------------------------------------------------------------------------------

#Note to self add a \n inside the string to get spacing.
