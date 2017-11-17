from sys import argv #sys is a package argv is module

script, filename = argv

txt = open(filename) #create a file object

print(f"Here's your file {filename}:")
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
