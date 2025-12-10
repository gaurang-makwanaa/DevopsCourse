
score = int(input("Enter your Grade: \n"))
# Take input 

# Determine grade
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

# Print Grade
print("Your grade is:", grade)
