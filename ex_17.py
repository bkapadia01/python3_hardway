from sys import argv
from os.path import exists

script, from_file, to_file =argv

print(f"copying from {from_file} to {to_file}")

#we could do these in one line?
in_file = open(from_file).read()

print(f"the inpout file is {len(in_file)} bytes long")
print(f"does the output file exist? {exists(to_file)}")
# print("ready, hit, return to conitnue or ctrl-C to cancel")
# input() 

out_file = open(to_file, 'w').write(in_file)

print("alright all done")

