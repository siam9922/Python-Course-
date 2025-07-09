
#--------------------------------------------------------------------------------------------------------------------------------------------------------


'''

Project: Age in Months and Days
Idea:
You are given your age as a string, like "18".
You will:

Convert it to an integer

Calculate how many months and days you've lived (roughly)

Print it out nicely




'''
#--------------------------------------------------------------------------------------------------------------------------------------------------------

age_calculator = "Age Calculator\n"
print(age_calculator)


age = "18"

print(f"You are {int(age)} years old.\n")

description = "That means you've been alive for about:"
print(description)

months = 12
days = 365 

print(f"-{(int(age) * int(months))} months")
print(f"-{(int(age) * int(days))} days\n")


#--------------------------------------------------------------------------------------------------------------------------------------------------------
'''

Age Calculator

You are 18 years old.
That means you've been alive for about:
- 216 months
- 6570 days


'''
#--------------------------------------------------------------------------------------------------------------------------------------------------------