

# Variables to work with
math_score = 90
english_score = 92
science_score = 78
student_name = "John"
name = 5


# Create conditional expressions to:
# 1. Assign letter grade for math (A=90+, B=80+, C=70+, D=60+, F=below 60)
# 2. Assign letter gra`de for english 
# 3. Assign letter gra`de for science
# 4. Check if student name is short (less than 5 characters) or long
# 5. Determine if student is "Honor Roll" (all scores 85+) or "Regular"

# Print all results

#MATH, #ENGLISH, SCIENCE



name_check = "short name" if len(student_name) < 5 else "long"

letter_grade = "Honor Roll" if english_score >= 85 else "Regular"
print(letter_grade)

letter_grade = "Honor Roll" if math_score >= 85 else "Regular"
print(letter_grade)

letter_grade = "Honor Roll" if science_score >= 85 else "Regular"
print(letter_grade)





