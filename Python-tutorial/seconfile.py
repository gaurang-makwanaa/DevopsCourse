# Program to create a text file and write content to it

# Open a new text file in write mode
file = open("myfile1.txt", "w")

# Write content to the file
file.write("Hello, this is my first text file!\n")
file.write("Writing content using Python file handling.\n")
file.write("File functions: open() and write().")

# Close the file
file.close()

print("Content written successfully to myfile.txt!")
