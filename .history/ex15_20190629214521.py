from sys import argv
script, filename = argv

txt = open(filename)

print(f"heres your file {filename}")
print(txt.read())
close()
print ("type the file name agian:")
file_name = input('> ')

txt_again = open(file_name)
print(txt_again.read())
close()