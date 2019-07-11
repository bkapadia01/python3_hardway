def cheese_crackers (cheese_count, boxes_cracker):
    print(f"you have {cheese_count} cheesess!")
    print(f"you have {boxes_cracker} boxes of crackers!")
    print("this is a new line under me \n")

print("we can give the functions numbers directly:")
cheese_crackers(10,20)

print("or we can use variable from this script")
amount_of_cheese = 30
amount_of_crakcers = 40

cheese_crackers(amount_of_cheese, amount_of_crakcers)

print("we can even do some math and assign to variables")
cheese_crackers(10+20, 30+40)

print("and we can combine the tewo vairalbes and math")
cheese_crackers(amount_of_cheese+100, amount_of_crakcers+200)
