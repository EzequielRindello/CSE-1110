# Take the grade student
grade = int(input("What is your grade percent? "))
# Statements
if grade >= 90:
    letter = "A"
elif grade >= 80:
    letter = "B"
elif grade >= 70:
    letter = "C"
elif grade >= 60:
    letter = "D"
else:
    letter = "F"
# Print the result
print(f"Your letter grade is: {letter}")
# Aditional message
if grade >= 70:
    print("Congratulations! You passed the class!")
else:
    print("Stay focused and you'll get it next time!")
