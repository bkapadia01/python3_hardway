#implicit inheritace

class Parent(object):
    def implicit(self):
        print ("parent implicit()")

class Child(Parent):
    def implicit(self):
        print("child override()")

dad = Parent()
son = Child()

dad.implicit()
son.implicit()
