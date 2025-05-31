#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Exercise 3: Typecasting
#TypeCasting = the process of converting a value from one data type to another.
#Ex: int, float, str, bool
#Typecasting is useful when you need to perform operations on different data types or when you want to ensure that a value is in the correct format for a specific operation.
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

name = "Siam Hasan"
age = 23
gpa = 3.1
is_Student = True

#How it works the type function
print(type(name))
print(type(age))
print(type(gpa))
print(type(is_Student))

#How to convert

gpa = int(gpa)
print(gpa)

#age = float(age)
#cleprint(age)

name = bool(name)
print(name)

#You can change it or figure out what data type it is 
age = str(age)
#print(type(age))

#Since we are working with strings the number changes to string

age += "1"
print(age)

name = bool(name)
print(type(name))


#Re-watching

name = "Danial Larusso"
age = "41"
gpa = 1.6
is_student = False

age += "1"

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))


gpa = int(gpa)
print(gpa)

name = bool(name)
print(name)

age = str(age)
print(age)
(print(type(age)))