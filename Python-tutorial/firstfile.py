# Program to create a text file and write content to it

# Ask user for the file name
file = open("myfile.txt", "w")

# Open the file in write mode and write content

file.write("Hello! This is my first file.\n")
file.write("I am learning Python file handling.\n")
file.write("This content is written using Python.\n")

file.close()

print("Content written successfully to myfile.txt!")
