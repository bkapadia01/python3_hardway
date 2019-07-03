# this is like argv script

def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

#so *args is pointless ->

def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2:{arg2}")

#this takes 1 statement
def print_one(arg1):
    print(f"arg1:{arg1}")

#takes no args
def print_none():
    print("i do nothing")

print_two("zed", "shaw")
print_two_again("zeddy", "shawy")
print_one("onlyone")
print_none()
