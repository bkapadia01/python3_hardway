number = []



def while_func(i,j,k):
    while i < j:
        print(f"at the top i is {i}")
        number.append(i)

        i += k
        print("number is now", number)

        print(f"at the bottom i is: {i}")

print("the numbers: ")
while_func(0, 5, 2)
for num in number:

    print(num)
