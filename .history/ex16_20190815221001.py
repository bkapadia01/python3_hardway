from sys import argv
script, filename = argv

print(f"we're going to erase {filename}")
print(f"if you don't want that hit ctrl C")
print(f"if you do want that hit return")
input("?")

print("opening the file...")
target = open(filename, "w")

print("truncating the file goodbye...")
target.truncate()

print("now im going to ask you for 3 lines")

line1 = input("line 1: ")
line2 = input("line 2:")
line3 = input("line 3:")

print("im going to write these lines to a file")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.close()

file_name = open(filename) 
print("now i will read it back to you")

print(file_name.read())
print("and finally we close it")
input("enter to close")



