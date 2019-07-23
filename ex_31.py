print("""you enter a dark room
do you go through door 1 or 2?""")

door = input("> ")

if door == "1":
    print ("giant better eatting cheese")
    print("what do you do?")
    print("1. take cake, 2. scream at bear")

    bear = input("> ")

    if bear == "1":
        print ("beart eats you")
    elif bear == "2":
        print("the bear eats you")
    else:
        print(f"doing {bear} is prob the best")
        print("bear rusn away")

elif door == "2":
    print("you stare in to the abyss")
    print("1. blue berries")
    print("2. yello jacket cllothin")
    print("3. understaind rev. yelling melodies")

    insanity = input("> ")
    if insanity == "1" or insanity == "2":
        print("youbody survies powerd by jello")
        print("good job")
    else:
        print("insanity rots you")

else:
    print("you stumble, fall and die")
