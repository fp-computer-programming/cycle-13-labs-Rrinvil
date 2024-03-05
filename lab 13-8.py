# Create a handle to open a file for writing called my_file.txt
with open('my_file.txt', 'w') as file:
    # Add 3 lines to the file
    file.write("Your Initials - Today's Date\n")
    file.write("Hello World!\n")
    file.write("What you have been doing for fun\n")

# The file will be automatically closed after the with block

# Confirm that a file called my_file.txt appears in the same folder as the Python file
# Run the Python script to generate the file