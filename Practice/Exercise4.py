
#Practice 1

'''

#Calculate the area of a rectangle 

print ("What is the area of a rectangle?")

length = float(input("Enter a value for length: "))
width =  float(input("Enter a value for width: "))



area= length * width

print(f"Congratulations the area is {area}")

'''



#Practice2

#Shopping Cart program 

item = str(input("What item would you like to buy? "))
quantity1 = int(input("How many are you buying? "))

#item2 = str(input("Pick another item! "))
#quantity1 = int(input("How many are you buying? "))


price1 = float(12.00)
price1 = price1 * quantity1

print(f"You have bought {item} x {quantity1} number of items")
print(f"The total price of {item} is ${price1}.")