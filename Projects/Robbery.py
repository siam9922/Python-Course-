
#Robbery Project 
#Create a decision making choice to either give money to robber or not 

#--------------------------------------------------------------------------------------------------------------------------------------------------------

name = input("Give me your money! (How much money will you give?) ") 
decision =  input("(Choice 1 or Choice 2)")


decision1 = 1
decision2 = 2

choice1 = (f"Yes here it is! I will give you ${name}!")
choice2 = ("Please I am homeless I don't have money") 


if decision1:
    print(f"{choice1}")
else:
    print(f"{choice2}")

#--------------------------------------------------------------------------------------------------------------------------------------------------------