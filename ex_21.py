def add(a,b):
    print(f"adding {a} + {b}")
    return a + b

def subtract(a,b):
    print(f"subtract {a} - {b}")
    return a - b

def multiply(a,b):
    print(f"multiply {a} * {b}")
    return a * b

def divide(a,b):
    print(f"divide {a} / {b}")
    return a / b

print ("lets do some math with just functions")
x = float(input("whats your value for x "))
y = float(input("whats your value for y "))

agex = add(x,y)
print(f"adding x an y gives you {agex}")
age = add(20, 5)
height = subtract(20, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"age: {age}, height: {height}, weight: {weight}, iq: {iq}")

#puzzle
print("here's a puzzle")
what = add(age, subtract(height,multiply(weight, divide(iq, 2))))
print("what beocmes:", what, "Can you do it hand?")
