# Program to read and display content from a text file

# Open the file in read mode
file = open("myfile.txt", "r")

# Read the entire content of the file
content = file.read()

# Print the content
print("File Content:\n")
print(content)

# Close the file
file.close()
