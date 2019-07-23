from sys import exit

def gold_room():
    print("this room is full of gold, how much do you take?")

    choice = input('> ')
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("type a number")

    if how_much < 50:
        print("okay greedy. you win")
        exit(0)
    else:
        dead("too greedy you dead")

def bear_room():
    print("bear in a room, how are you going to pass the bear")
    bear_moved = False

    while True:
        choice = input("> ")
        if choice == "take honey":
            dead("the bear kills you")
        elif choice == "taunt bear" and not bear_moved:
            bear_moved = True
            print("the bear moved you're free")
        elif choice == "taunt bear" and bear_moved:
            dead("the bar gets pissed and kills you")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("i dont know waht that means")

def chulu_room():
    print("here is the evil chulu")
    print("when you look at it you go insane, how do you escape?")
    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("well that was tasty")
    else:
        chulu_room()

def dead(why):
    print(why, ". good job")
    exit(0)

def start():
    print("you're in dark room, choose left or right door")

    choice = input("> ")
    if choice == "left":
        bear_room()
    elif choice == "right":
        chulu_room()
    else:
        dead("you are lost and you die")    

start()