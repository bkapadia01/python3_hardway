ten_things = "apples oramnges crwos telephone sugar light"

print("thats not 10 things, thats only 6")

stuff = ten_things.split(" ")
more_stuff = ["day", "nifght", "song", "frisbee", "Corn", "banana", "girl", "boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("adding:", next_one)
    stuff.append(next_one)
    print(f"there are {len(stuff)} items npw")

print("there we go:", stuff)

print("lets do some things with htis list")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(stuff[-1])
print(' '.join(stuff))
print('#'.join(stuff[3:5]))
