#Exercise 2 Practice


'''
user_name : Bro Code
year = 2025
pi = 3.14
is_ admin = true 
'''

user_name = "Bro Code"
print(f"His username is {user_name}.")

year = 2025
print(f"My little cousin was born in the year {year}.")

pi = 3.14
print(f" The formula needs to use {pi} to calculate this equation.")

is_admin = True

if is_admin:
    print("He is the discord admin of Clash of clans")
else:
    print("He is NOT the admin of Clash of clans ")



#Python Practice after 1 month

#1.

name = "Siam"
print("My name is Siam")  

#2.

#How indexing works
'''s = "string"
print(f"{s}"[0])
print(f"{s}"[5])

'''

#3. 

# String Slicing works 
#For future self: Slicing works like this it follows a method Start:Stop:Step
#Start is the start of the index you want to slice Ex. string is "Champion" ---- print(s[0:5]) -----> Output = "champ"
#Stop is the part of the slice you want to stop Ex. string 
#Step is where you skip letters ---> "print(s[0:4:3])" I tried this if you change step it will skip letters
s = "Programming"
print(s[3:7])
print(s[0:3])
print(s[0:4:3])
print(s[8:11])


#4.

#Using len function to find the length of a string

s = "Print"
x = len(s)
print(f"{x}")

s = "Olatunji"
x = len(s)
print(x)


#5

#Concatanate string 


#Practice

going_to_gym = True

if going_to_gym:
    print("I can't read atomic habits")
else:
    print("I can read Atomic Habits")


    user_name = "G-one61"
    year = 2002
    pi = 3.14
    is_admin = True

    print(f"Your username is {user_name}")
    print(f"You were born in {year}.")
    print(f"You found your age by using a complex formula of {pi}")
    
    if is_admin:
        print("You are my boss!")
    else:
        print("You are not the boss!")