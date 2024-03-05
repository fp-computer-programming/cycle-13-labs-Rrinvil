# Create a dictionary named grades with assignment names as keys and grades out of 100 as values
grades = {'assignment1': 85, 'assignment2': 92, 'assignment3': 60, 'assignment4': 45}

# Print a list of just all the grades received using a one-line statement
print(list(grades.values()))

# Print the name of each assignment in the dictionary on a separate line using a loop
for assignment in grades:
    print(assignment)

# Print the name and grade received on each assignment with a score of 70 or above using a loop
for assignment, grade in grades.items():
    if grade >= 70:
        print(f"{assignment}: {grade}")

# Print the name and grade received on each assignment with a score of 50 or below using a loop
for assignment, grade in grades.items():
    if grade <= 50:
        print(f"{assignment}: {grade}")