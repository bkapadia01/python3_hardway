#implicit inheritace

class Parent(object):
    def altered(self):
        print ("parent implicit()")

class Child(Parent):
    def altered(self):
        print("child override()")

dad = Parent()
son = Child()

dad.altered()
son.altered()
