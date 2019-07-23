#this is a dictonary
mystuffs = {'apple': "I AM APPLE"}
print(mystuffs['apple'])


#import the modules/functions from other files
import mystuff
import myfruits

#from the mystuff.py file with function apple()
mystuff.apple()
print(mystuff.tangerine)

class MyStuffB(object):
    def __init__(self):
        self.tangrine = "and now million years"
    
    def apple(self):
        print("i am apple in teh same basket")


#obtain class modules from the save file
thing = MyStuffB()
thing.apple()
print(thing.tangrine)

#obtain class from a file called "myfruits"
fruits = myfruits.MyFruits()
fruits.apple()
print(fruits.tangerine)

