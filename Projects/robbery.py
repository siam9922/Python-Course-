

"""

🔧 Your Task:
Ask for the user’s name (just for personalization).

Tell the user: "A masked robber approaches you and yells: 'Give me your money!'"

Show them 3 choices:

1: Give the money

2: Refuse to give the money

3: Try to run

Based on their input:

If they pick 1, print a scared response + amount given (ask for how much).

If they pick 2, print what happens when they refuse (maybe the robber gets angry).

If they pick 3, print a random outcome like "you escape" or "you trip and fall" (optional: use random module later).



"""

#--------------------------------------------------------------------------------------------------------------------------------------------------------

introduction = "Welcome to the Decision-Making Game!"
print(introduction)

name = input("\nWhat is your name? ")
print(f"\nHello {name}. A masked robber approaches you and yells: 'Give me your money!")

question = "\nWhat will you do?"
print(question)


print("\nA. Give the money")
print("B. Refuse to give money")
print("C. Try to run")

choices = str(input("\nPick one of the three choices! (Type 'A' 'B' 'C') "))

if choices == "A":
    print("How.....much money do you want?")
elif choices == "B": 
    print("How dare you?! Shoots civilian.")
elif choices == "C": 
    print("You escaped")
else:
    print("Invalid choice. The robber is confused.")







#--------------------------------------------------------------------------------------------------------------------------------------------------------