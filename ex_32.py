#loops and lists
count = [1, 2, 3, 4, 5]
fruits = ['apple','oranges','pears','apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for number in count:
    print (f"this is count {number}")

for fruit in fruits:
    print(f"a fruit types: {fruit}")

# also can go through mixed lists, notice we have to use {} since we dont knowwhat's in it

for i in change:
    print(f"i got: {i}")

#build list
elements = []

#range function to do 0-5 count
for i in range(0,6):
    print(f"adding {i} to to the list")
    elements.append(i)

for i in elements:
    print(f"element was {i}")