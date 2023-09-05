# Read from the file
with open("nameOfFile.txt", "r") as file:
    data = file.read()

print(data)

#----------------------------------------------

# Write back to the file
with open("nameOfFile.txt", "w") as file:
    file.write("Hello")

