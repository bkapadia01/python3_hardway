type_people = 10
x = f"there are {type_people} types of people"

binary = "binary"
do_not = "don't"
y = f"those who know {binary} and those who {do_not}"

print(x)
print(y)

print(f"i said {x}")
print(f"i said '{y}'")

hilarious = False
joke = "Is that joke funny?! {}"

print(joke.format(hilarious))
w = "this is the left of ...."
e = "a string with a right side"

print(w + e)
print("." * 10)

end1 = "X"
end2 = "ray"

print(end1+ '-' + end2)
print("it's fleece was as white as {} {}".format('snow','help'))